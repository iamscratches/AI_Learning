# AI Learning Roadmap

This is the maintained, sequential knowledge base for the local-first AI learning path. It records confirmed learning, practical work, resources, gaps, and recommended next steps without treating progress as a chronological log.

## Learning Domain: Local-First AI Engineering

### Stage 0 — Local AI Lab Setup

**Status:** In progress

**Purpose:** Establish a repeatable local environment for the later LLM, application, RAG, agent, evaluation, and safety modules.

#### Confirmed setup and practical work

- Created the Git repository [iamscratches/AI_Learning](https://github.com/iamscratches/AI_Learning) to store learning progress and project work.
- Installed Ollama locally using the download instructions from [Ollama](https://ollama.com/download).
- Ran a basic local command to confirm that Ollama is installed.
- Chose the existing Rancher Desktop installation as the container runtime for this learning environment rather than Docker Desktop.
- Recreated the Transformers course virtual environment with Homebrew Python, confirming a usable local Python setup.

#### Resources

- [Free, Local-First AI Learning Roadmap](free-local-first-ai-learning-roadmap.md) — source curriculum and Stage 0 setup requirements.
- [Ollama download](https://ollama.com/download) — local Ollama installation source.
- [AI_Learning GitHub repository](https://github.com/iamscratches/AI_Learning) — project-learning progress repository.

#### Current understanding and boundaries

- Ollama is installed and its basic local availability has been checked.
- No model has been downloaded, integrated, or invoked through Ollama yet.
- Rancher Desktop is the chosen Docker-compatible environment; its availability for this roadmap has not yet been confirmed.

#### Dependencies and open items

- Create the required `learning-journal.md` file in the exercise repository, if it is not already present.
- Select and download a suitable local Ollama model.
- Run a command-line prompt successfully and document the result; this completes the Stage 0 deliverable.
- Confirm Rancher Desktop can run the required container workflow when a later module needs it.

#### Recommended next step

Download one small Ollama model appropriate for the available hardware, then run a simple command-line prompt and record the exact command, model name, result, and any issue encountered in `learning-journal.md`.

### Stage 1 — LLM Fundamentals

**Status:** In progress — basic Transformers pipeline practice complete

**Purpose:** Build a local Python and Transformers foundation for learning the mechanics and use of language models.

#### Confirmed setup and practical work

- Followed the Hugging Face LLM Course setup instructions and chose a local Python environment instead of Google Colab.
- Created the course virtual environment at `/Users/suvnkr/Desktop/own/AI_Learning/transformersCourse/.env`.
- Installed the Transformers dependency with sentencepiece support using `pip install "transformers[sentencepiece]"`.
- Installed PyTorch using `python -m pip install torch`.
- Installed or upgraded Pillow and torchvision inside the virtual environment using `python -m pip install --upgrade Pillow torchvision`.
- Identified FFmpeg as an additional macOS host dependency, installable with `brew install ffmpeg`.
- Opened an interactive Python terminal and ran some examples from the Hugging Face LLM Course's Chapter 1, section 2.
- Watched the Hugging Face LLM Course introductory video.
- Tested `transformerLibsExamples1.py` both outside and inside the course virtual environment.
- Completed the basic Transformers examples in [transformerLibsExamples1.py](transformersCourse/transformerLibsExamples1.py) and [transformerLibsExamples2.py](transformersCourse/transformerLibsExamples2.py), using the current numbered sequence.

#### Example index

| Example | Topic |
| --- | --- |
| 1–2 | Sentiment analysis for one input and a batch of inputs |
| 3 | Zero-shot classification |
| 4–5 | Text generation with a default pipeline and a selected Hub model |
| 6 | Fill-mask prediction |
| 7 | Named-entity recognition |
| 8 | Context-grounded question answering with a chat prompt |
| 9 | Summarization |
| 10 | Translation |
| 11 | Image classification |
| Additional demonstration | Automatic speech recognition with Whisper |

#### Basic Transformers learning summary

- `pipeline()` is the high-level Hugging Face abstraction that combines preprocessing, model inference, and postprocessing behind a task-oriented interface.
- A pipeline can use a default pretrained model for a task or a specifically named model from the Hugging Face Hub. Downloaded models are cached for later reuse.
- Practiced sentiment analysis for individual and batched text, interpreting the returned label and confidence score.
- Practiced zero-shot classification, providing candidate labels at inference time rather than fine-tuning a classifier for those labels.
- Practiced text generation from a prompt and controlled it with parameters such as `max_length`, `num_return_sequences`, and `max_new_tokens`. Generation can vary because it is not inherently deterministic.
- Practiced fill-mask prediction, which ranks likely replacements for a `<mask>` token.
- Practiced named-entity recognition with `aggregation_strategy="simple"`, returning grouped person, organization, and location entities with their spans and scores.
- Used an instruction-tuned chat model (`Qwen/Qwen2.5-0.5B-Instruct`) with structured `system` and `user` messages for context-grounded question answering, summarization, and translation.
- Used the image-classification pipeline with a Vision Transformer model and the automatic-speech-recognition pipeline with Whisper, showing that the same pipeline pattern extends beyond text.
- Suppressed nonessential library logs and download progress during examples with `transformers.utils.logging`.

#### Practical interpretation notes

- The context-based question-answering example is generative: the model produces an answer from the supplied context and instructions. It is not a guaranteed extractive lookup, so its output should still be checked against the context.
- The commented outputs are illustrative. Exact labels, rankings, scores, and generated text can change with model versions, model configuration, and generation settings.

#### Environment test and observation

- With `.env` deactivated, running `python transformerLibsExamples1.py` raised `ModuleNotFoundError: No module named 'transformers'`.
- With `.env` activated, the same script ran without error and `which python` resolved to `/Users/suvnkr/Desktop/own/AI_Learning/transformersCourse/.env/bin/python`.
- After deactivation, `which python` resolved to `/Users/suvnkr/.local/bin/python`.

**Takeaway:** Python packages are environment-specific. Activating the course `.env` selects the interpreter that contains the installed Transformers dependencies; the separately resolved user-level Python does not have that package available.

#### Debugging note: repaired virtual environment

The original `.env` was created from a broken or relocated `uv` Python installation (`sys.base_prefix = /install`). It could not locate Python's standard library, including `encodings`. Reinstalling Homebrew Python alone did not repair that already-created environment.

The environment was recreated explicitly with Homebrew Python:

```bash
rm -rf .env
brew reinstall python
"$(brew --prefix python)/bin/python3" -m venv .env
source .env/bin/activate
python -m pip install --upgrade pip
```

Use the following command to confirm that an active environment uses Homebrew Python rather than `uv`:

```bash
python -c "import sys; print(sys.executable); print(sys.base_prefix)"
```

#### Resources

- [Hugging Face LLM Course: setup](https://huggingface.co/learn/llm-course/chapter0/1) — local-environment setup guidance.
- [Hugging Face LLM Course: Chapter 1, section 2](https://huggingface.co/learn/llm-course/chapter1/2) — executed example source.
- [Hugging Face LLM Course introductory video](https://www.youtube.com/watch?v=00GKzGyWFEs) — introductory course overview.
- [Learner notes: How Transformers Work](transformersCourse/transformers-how-they-work-notes.md) — completed summary of Hugging Face LLM Course Chapter 1, section 4.
- [Hugging Face LLM Course: How do Transformers work?](https://huggingface.co/learn/llm-course/chapter1/4) — source material for the learner notes.
- [Learner notes: How Transformers Solve Tasks](transformersCourse/transformers-task-solving-notes.md) — completed summary of Hugging Face LLM Course Chapter 1, section 5.
- [Hugging Face LLM Course: How 🤗 Transformers solve tasks](https://huggingface.co/learn/llm-course/chapter1/5) — source material for the learner notes.
- [Learner notes: Transformer Architectures](transformersCourse/transformer-architectures-notes.md) — completed summary of Hugging Face LLM Course Chapter 1, section 6.
- [Hugging Face LLM Course: Transformer Architectures](https://huggingface.co/learn/llm-course/chapter1/6) — source material for the learner notes.

#### Current understanding and boundaries

- A local Python environment for the Transformers course is available and has the listed dependencies installed.
- The relationship between virtual-environment activation, interpreter selection, and package availability has been practically verified.
- Some Chapter 1, section 2 examples were executed interactively.
- Specific examples, their outputs, and the concepts confirmed by those runs have not yet been recorded.
- Completed the Chapter 1, section 4 reading on Transformer pretraining, transfer learning, attention, architecture families, and checkpoints; see the linked learner notes.
- Completed the Chapter 1, section 5 reading on how task inputs, model architectures, task heads, and outputs fit together across language, audio, and vision; see the linked learner notes.
- Completed the Chapter 1, section 6 reading on architecture selection and attention variants for long inputs; see the linked learner notes.

#### Dependencies and open items

- Record the particular examples run, observed outputs, and any questions or errors.
- Install and verify FFmpeg with `brew install ffmpeg` when it is needed; successful installation has not yet been confirmed.
- Continue the curriculum's LLM fundamentals topics: tokens, prompts, context, structured output, embeddings, inference, and model limitations.
- Use the local setup to connect the course work to the separate Ollama model-delivery requirement from Stage 0.

#### Recommended next step

Repeat one Chapter 1, section 2 example in a saved script or notebook, then document the code's purpose, its output, and the concept it demonstrates before moving to the next course section.

### Upcoming Sequence

1. Basic local AI application: API and simple interface.
2. RAG fundamentals, evaluation, controlled tool workflows, agents, test automation, performance analysis, security, and safe SDLC integration.

See the [source learning roadmap](free-local-first-ai-learning-roadmap.md) for the detailed module sequence and supplied resources.
