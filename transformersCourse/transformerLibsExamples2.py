from transformers import pipeline
from transformers.utils import logging
logging.set_verbosity_error()
logging.disable_progress_bar()

# 6.
# Mask Filling:
# The idea of this task is to fill in the blanks in a given text
unmasker = pipeline("fill-mask")
confidence = unmasker("This course will teach you all about <mask> models in <mask>.", top_k=2)
# print(confidence)

# Output: 
# [{'score': 0.19619974493980408, 'token': 30412, 'token_str': ' mathematical', 'sequence': 'This course will teach you all about mathematical models.'}, {'score': 0.04052743315696716, 'token': 38163, 'token_str': ' computational', 'sequence': 'This course will teach you all about computational models.'}]

# ===========================================================================================

# 7.
# Named entity recognition:
# Named entity recognition (NER) is a task where the model has to find which parts of the input text correspond to entities such as persons, locations, or organizations.

ner = pipeline("ner", aggregation_strategy="simple")
confidence = ner("My name is Sylvain and I work at Hugging Face in Brooklyn.")
# print(confidence)

# Output: 
# [{'entity_group': 'PER', 'score': np.float32(0.9981694), 'word': 'Sylvain', 'start': 11, 'end': 18}, {'entity_group': 'ORG', 'score': np.float32(0.9796019), 'word': 'Hugging Face', 'start': 33, 'end': 45}, {'entity_group': 'LOC', 'score': np.float32(0.9932106), 'word': 'Brooklyn', 'start': 49, 'end': 57}]

# ===========================================================================================

# 8.
# Question answering:
# Instead of extracting a snippet from a text, modern models answer questions by reading the context inside a prompt. You can use a lightweight, efficient chat model like Qwen/Qwen2.5-0.5B-Instruct or meta-llama/Llama-3.2-1B-Instruct

generator = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B-Instruct")
# Structure it as a conversational chat prompt
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant. Use the provided context to answer the question briefly.",
    },
    {
        "role": "user",
        "content": "Context: My name is Sylvain and I work at Hugging Face in Brooklyn\nQuestion: Where do I work?",
    },
]

result = generator(messages, max_new_tokens=20)
# print(result)

# Output: 
# [{'generated_text': [{'role': 'system', 'content': 'You are a helpful assistant. Use the provided context to answer the question briefly.'}, {'role': 'user', 'content': 'Context: My name is Sylvain and I work at Hugging Face in Brooklyn\nQuestion: Where do I work?'}, {'role': 'assistant', 'content': 'Hugging Face in Brooklyn'}]}]

# Note that this pipeline works by extracting information from the provided context; it does not generate the answer.

# ===========================================================================================

# 9.
# Summarization :
# Initialize using the modern 'text-generation' task with a chat/instruct model
generator = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B-Instruct")

text_to_summarize = """
   America has changed dramatically during recent years. Not only has the number of graduates in traditional engineering disciplines such as mechanical, civil, electrical, chemical, and aeronautical engineering declined, but in most of the premier American universities engineering curricula now concentrate on and encourage largely the study of engineering science. As a result, there are declining offerings in engineering subjects dealing with infrastructure, the environment, and related issues, and greater concentration on high technology subjects, largely supporting increasingly complex scientific developments. While the latter is important, it should not be at the expense of more traditional engineering.

    Rapidly developing economies such as China and India, as well as other industrial countries in Europe and Asia, continue to encourage and advance the teaching of engineering. Both China and India, respectively, graduate six and eight times as many traditional engineers as does the United States. Other industrial countries at minimum maintain their output, while America suffers an increasingly serious decline in the number of engineering graduates and a lack of well-educated engineers.
"""

# Format your input as a structured prompt or chat template
messages = [
    {"role": "user", "content": f"Summarize the following text:\n\n{text_to_summarize}"}
]

# Run inference
result = generator(messages, max_new_tokens=15)

# print(result)

# Output: 
# [{'generated_text': [{'role': 'user', 'content': 'Summarize the following text:\n\n\n    America has changed dramatically during recent years.Not only has the number of \n    graduates in traditional engineering disciplines such as mechanical, civil, \n    electrical, chemical, and aeronautical engineering declined, but in most of \n    the premier American universities engineering curricula now concentrate on \n    and encourage largely the study of engineering science. As a result, there \n    are declining offerings in engineering subjects dealing with infrastructure, \n    the environment, and related issues, and greater concentration on high \n    technology subjects, largely supporting increasinglycomplex scientific \n    developments. While the latter is important, it should not be at the expense \n    of more traditional engineering.\n\n    Rapidly developing economies such as China and India, as well as other \n    industrial countries in Europe and Asia, continue to encourage and advance \n    the teaching of engineering. Both China and India, respectively, graduate \n    six and eight times as many traditional engineers as does the United States. \n    Other industrial countries at minimum maintain their output, while America \n    suffers an increasingly serious decline in the number of engineering graduates \n    and a lack of well-educated engineers.\n'}, {'role': 'assistant', 'content': 'The author discusses how engineering education in the United States has shifted towards more technical'}]}]


# ===========================================================================================

# 10.
# Translation :
# For translation, you can use a default model if you provide a language pair in the task name (such as "translation_en_to_fr"),
translator = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B-Instruct")

text_to_translate = "Ce cours est produit par Hugging Face."

# Format your input as a structured prompt or chat template
messages = [
    {"role": "user", "content": f"Translate the following text from french to english:\n\n{text_to_translate}"}
]

# Run inference
result = generator(messages)

# print(result)
# Output:
# [{'generated_text': [{'role': 'user', 'content': 'Translate the following text from french to english:\n\nCe cours est produit par Hugging Face.'}, {'role': 'assistant', 'content': 'This course is produced by Hugging Face.'}]}]


# ===========================================================================================

# 11. 
# Image and audio pipelines:

# Image classification:
image_classifier = pipeline(
    task="image-classification", model="google/vit-base-patch16-224"
)
result = image_classifier(
    "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg"
)
# print(result)

# Output:
# [{'label': 'lynx, catamount', 'score': 0.4333997368812561}, {'label': 'cougar, puma, catamount, mountain lion, painter, panther, Felis concolor', 'score': 0.03480527177453041}, {'label': 'snow leopard, ounce, Panthera uncia', 'score': 0.03240463510155678}, {'label': 'Egyptian cat', 'score': 0.023973943665623665}, {'label': 'tiger cat', 'score': 0.022902335971593857}]

# Automatic speech recognition
transcriber = pipeline(
    task="automatic-speech-recognition", model="openai/whisper-large-v3"
)
result = transcriber(
    "https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac"
)
# print(result)

# Output:
# {'text': ' I have a dream that one day this nation will rise up and live out the true meaning of its creed.'}