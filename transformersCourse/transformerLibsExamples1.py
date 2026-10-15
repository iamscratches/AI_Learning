import transformers
from transformers import pipeline

# 1.
# The most basic object in the 🤗 Transformers library is the pipeline() function. 
# It connects a model with its necessary preprocessing and postprocessing steps, 
# allowing us to directly input any text and get an intelligible answer:
classifier = pipeline("sentiment-analysis")
confidence = classifier("I've been waiting for a HuggingFace course my whole life.")
# print(confidence)
# Output: [{'label': 'POSITIVE', 'score': 0.9598047137260437}]

# ===========================================================================================

# 2.
# We can even pass several sentences!
# By default, this pipeline selects a particular pretrained model that has been fine-tuned 
# for sentiment analysis in English. The model is downloaded and cached when you create
# the classifier object. If you rerun the command, the cached model will be used instead 
# and there is no need to download the model again.
#
# There are three main steps involved when you pass some text to a pipeline:
# a. The text is preprocessed into a format the model can understand.
# b. The preprocessed inputs are passed to the model.
# c. The predictions of the model are post-processed, so you can make sense of them.

confidence = classifier(
    ["I've been waiting for a HuggingFace course my whole life.", "I hate this so much!"]
)
# print(confidence)
# Output: 
# [{'label': 'POSITIVE', 'score': 0.9598047137260437}]
# [{'label': 'POSITIVE', 'score': 0.9598047137260437}, {'label': 'NEGATIVE', 'score': 0.9994558691978455}]

# ===========================================================================================

# 3. 
# Zero-shot classification:
# We’ll start by tackling a more challenging task where we need to classify texts that
# haven’t been labelled. This is a common scenario in real-world projects because annotating
# text is usually time-consuming and requires domain expertise. For this use case, the 
# zero-shot-classification pipeline is very powerful: it allows you to specify which labels 
# to use for the classification, so you don’t have to rely on the labels of the pretrained 
# model. You’ve already seen how the model can classify a sentence as positive or negative 
# using those two labels — but it can also classify the text using any other set of labels 
# you like.

classifier = pipeline("zero-shot-classification")
confidence = classifier(
    "This is a course about the Transformers library",
    candidate_labels=["education", "politics", "business"],
)

# print(confidence)

# Output:
# {'sequence': 'This is a course about the Transformers library', 
#  'labels': ['education', 'business', 'politics'], 
#  'scores': [0.8445951342582703, 0.1119769886136055, 0.043427880853414536]}
#
# This pipeline is called zero-shot because you don’t need to fine-tune the model on 
# your data to use it. It can directly return probability scores for any list of labels 
# you want!

# ===========================================================================================

# 4. 
# Text generation:
# Now let’s see how to use a pipeline to generate some text. The main idea here is that you 
# provide a prompt and the model will auto-complete it by generating the remaining text. 
# This is similar to the predictive text feature that is found on many phones. Text 
# generation involves randomness, so it’s normal if you don’t get the same results as shown 
# below.
generator = pipeline("text-generation")
generated_text = generator("In this course, we will teach you how to")
# print(generated_text)

# Output:
# [{'generated_text': "In this course, we will teach you how to write Python code for data analysisusing the Pandas library. We will start by setting up a basic environment with Python and Pandas and then dive into the fundamentals of Pandas, including data structures, data manipulation, and data visualization. You will learn how to load and manipulate data, perform data cleaning, and create data visualizations. Throughout the course, you will work on practical examples and exercises to help you apply your new skills. By the end of the course, you will have a solid foundation in data analysis with Pandas and be ready to tackle more advanced topics. Prerequisites: Basic understanding of Python programming concepts, such as variables, data types, and control structures. You should have a computer with Python and Pandas installed. The course will be taught using Jupyter notebooks, which allow you to write and execute code in a web browser. You will need to have Python 3.7 or later installed on your computer. You should also have a basic understanding of data analysis concepts, such as variables, data types, and data structures. The course will not cover data visualization libraries such as Matplotlib or Seaborn. However, you will learn how to use Pandas to create basic visualizations using the Pandas library's built-in plotting functions. You will"}]

# ===========================================================================================

# 5. 
# Using any model from the Hub in a pipeline:
# Model hub link: https://huggingface.co/models
generator = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-360M")
generated_text = generator(
    "In this course, we will teach you how to",
    max_length=30,
    num_return_sequences=2,
)
# print(generated_text)

# Output:
# [{'generated_text': 'In this course, we will teach you how to use the new language, while learning how to work with the existing language.\n\nThis course is not a language course. It is not a language course that helps you develop a new language. It is a language course that teaches you how to work with a new language.\n\nThis is not a language course that helps you learn a new language. It is a language course that helps you learn how to work with a new language.\n\nIt is a language course that helps you learn how work with a new language. It comes from a language course. It’s not a language course that helps you learn the language.\n\nIt’s a language course that helps you learn how you can work with a new language.\n\nIt’s not a language course that helps you learn a newlanguage. It is a language course that helps you learn how to work with a new language.\n\nIn other words, it’s a language course that helps you learn how to learn a new language.\n\nIt can be a language course that helps you learn a new language.\n\nBut it can also be a language course that helps you learn how work with a new language.\n\nIn other words, it has to be a language course that'}, {'generated_text': 'In this course, we will teach you how to do just this! This course will provide you with a solid foundation in the principles of geometry and trigonometry, and will buildupon your knowledge of these topics to help you become an accomplished engineer, architect, or designer.\n\nThis course is designed to be rigorous, yet accessible, so that even beginners can easily understand the concepts and get the most out of the material. You will learn about the fundamental building blocks of geometry, such as points, lines, and angles, as well as the concepts of distance, slope, and parallelism.\n\nYou will also learn about the fundamental building blocks of trigonometry, such as sine, cosine, and tangent, as well as the concepts of angle measures and right triangles. You will learn how to use these concepts to solve problems in engineering, architecture, and other fields.\n\nYou will learn how to use the Pythagorean theorem to find the length of a side in a right triangle, and how to use the sine, cosine, and tangent ratios to find the angle of a right triangle. You will also learn how to use the law of sines and the law of cosines to solve problems involving triangles.\n\nYou will learn how to use symmetry and transformation to solve problems in geometry. You will also learn how to use these concepts'}]
