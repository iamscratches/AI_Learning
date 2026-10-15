# How Transformers Work — Learner Notes

Source: [Hugging Face LLM Course — How do Transformers work?](https://huggingface.co/learn/llm-course/chapter1/4)

## Core ideas

- Transformer models are pretrained language models. They learn patterns from large quantities of raw text using self-supervised objectives, then can be adapted to a specific task through supervised fine-tuning.
- Two common pretraining objectives are causal language modeling, which predicts the next token from preceding context, and masked language modeling, which predicts hidden tokens.
- Reusing a pretrained model through transfer learning is usually far less data-, compute-, time-, and resource-intensive than training one from scratch. Choose a pretrained model close to the target task before fine-tuning it.
- Attention lets the model weigh which other tokens matter when building a representation for a token. Relevant context may be nearby or far away in the input.

## Model families and task fit

- **Encoder-only** models focus on understanding an input representation; they suit tasks such as classification and named-entity recognition.
- **Decoder-only** models generate tokens sequentially; they suit text generation.
- **Encoder-decoder** (sequence-to-sequence) models use an input representation to generate an output sequence; they suit tasks such as translation and summarization.
- In the original encoder-decoder Transformer, decoder self-attention is masked so that a generated position cannot inspect future target tokens. Decoder cross-attention can use the encoder’s input representation.

## Terminology to retain

- **Architecture:** the model’s structural design—its layers and operations.
- **Checkpoint:** a specific set of learned weights loaded into an architecture.
- **Model:** an informal term that can mean either architecture or checkpoint; be precise when the distinction matters.

## Practical connection

The task-specific `pipeline()` examples already practiced use pretrained checkpoints. The selected task and model family should match the problem: understand input, generate continuations, or transform one sequence into another.
