# Transformer Architectures — Learner Notes

Source: [Hugging Face LLM Course — Transformer Architectures](https://huggingface.co/learn/llm-course/chapter1/6)

## The three architecture families

- **Encoder-only:** uses complete input context. Choose it for classification, named-entity recognition, and extractive question answering. Examples: BERT and DistilBERT.
- **Decoder-only:** uses earlier tokens to predict the next token. Choose it for generation; modern LLMs commonly add instruction tuning after pretraining. Examples: SmolLM, Llama, and Gemma.
- **Encoder-decoder:** represents the whole input, then generates output left to right. Choose it for sequence transformation such as translation, summarization, grammar correction, and generative question answering. Examples: BART, T5, and Marian.

## Attention and long inputs

Standard full attention has quadratic cost as sequence length grows. Sparse variants reduce it: LSH attention selects likely relevant query-key pairs, local attention limits most tokens to a window, and axial positional encodings lower positional-representation memory needs.

## Practical connection

This architectural choice should precede selecting a pretrained checkpoint or a `pipeline()` task. The model family must fit the required information flow, not merely the task’s name.
