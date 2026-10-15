# How Transformers Solve Tasks — Learner Notes

Source: [Hugging Face LLM Course — How 🤗 Transformers solve tasks](https://huggingface.co/learn/llm-course/chapter1/5)

## Reusable task pattern

Transformer tasks follow a common flow: prepare an input representation, process it through an architecture suited to the task, attach an appropriate prediction head, and interpret the output. Pretraining supplies general representations; task-specific fine-tuning adapts them with comparatively little labelled data.

## Language tasks

- Encoder models such as BERT use bidirectional context and suit sequence classification, token classification, and extractive question answering. A task head maps hidden states to labels, token labels, or answer start/end positions.
- Decoder models such as GPT use masked self-attention and predict the next token from preceding tokens. Generation converts decoder states to vocabulary logits, then repeatedly selects the next token.
- Encoder-decoder models such as BART and T5 transform an input sequence into an output sequence. They suit summarization and translation; the decoder uses both earlier generated tokens and the encoder representation.

## Beyond text

- Whisper encodes audio representations and autoregressively generates text tokens for tasks such as transcription.
- Vision Transformers split an image into patches, treat patches as a sequence, add position information, and use a classification head over the resulting representation.

## Practical connection

The earlier `pipeline()` examples hide these implementation details. Select the pipeline, model family, and task head according to whether the job is understanding text, generating text, mapping one sequence to another, processing audio, or classifying images.
