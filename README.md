# 🤖 UNIP Face LLM

Vídeo demonstração

https://youtu.be/5Osk5lONvFo

Voice-based assistant with an animated face that integrates **Speech Recognition**, **Large Language Models (LLMs)** and **Text-to-Speech (TTS)** technologies, using **Vosk**, **Gemini**, and **Piper TTS**.

---

## Execution

```bash
python src/unip_face/main.py
```

---

## Abstract

**UNIP Face LLM** is an academic and experimental project developed within the context of **Universidade Paulista (UNIP)**. Its main objective is to integrate **Large Language Models (LLMs)** into a multimodal interactive interface, combining **Natural Language Processing (NLP)**, **Speech Recognition**, **Text-to-Speech (TTS)** synthesis, and **visual interaction through an animated avatar**.

The project explores concepts related to **Applied Artificial Intelligence**, **Conversational Systems**, **Human–Computer Interaction**, and **Modular Software Architectures**, serving as a foundation for academic studies, prototyping, and future research-oriented extensions.

---

## Project Objectives

The main objectives of the UNIP Face LLM project are:

* To investigate the practical application of **LLMs** in multimodal interactive systems.
* To integrate language models with **offline and online speech synthesis**.
* To explore **speech recognition techniques** applied to virtual assistants.
* To design a **modular, extensible, and well-documented architecture**.
* To serve as an **academic demonstrative project** for courses related to Artificial Intelligence, Robotics, and Intelligent Systems.

---

## Scope and Features

Currently, the project includes:

* Speech recognition using **Vosk**.
* Integration with **LLM APIs** (online mode).
* Voice synthesis using **Piper TTS** (local/offline execution).
* Modular project structure following software engineering best practices.
* Support for environment variables for secure configuration.
* A foundation for a visual interactive interface (animated face/avatar).

Planned or future features may include:

* Performance and response quality evaluation of language models.
* Integration with robotic systems or physical agents.
* Multi-language support.
* Instrumentation for academic data collection and evaluation metrics.

---

## Project Structure

The repository organization follows established software engineering practices:

```text
unip-face-llm/
├── assets/           # Visual resources, audio, and media files
├── docs/             # Technical and academic documentation
├── src/              # Main project source code
├── .env.example      # Example environment variable configuration
├── .gitignore        # Git ignored files and directories
├── README.md         # Main project documentation
└── requirements.txt  # Project dependencies
```

---

## System Requirements

* Python 3.10 or higher
* Linux environment (recommended)
* Dependencies listed in `requirements.txt`

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## Configuration

Sensitive configurations (such as API keys) must be defined using environment variables.

1. Copy the example environment file:

```bash
cp .env.example .env
```

2. Fill in the required values according to the execution environment.

---

## Methodology and Technical Approach

The project adopts a **modular design approach**, enabling:

* Clear separation between business logic, LLM integration, speech recognition, and interface layers.
* Ease of maintenance, testing, and extensibility.
* Reproducibility in academic and experimental contexts.

The use of **open-source technologies** encourages learning, critical analysis, and adaptation of the system to different research scenarios.

---

## Academic Applications

UNIP Face LLM may be used as:

* A supporting project for courses in Artificial Intelligence and Intelligent Systems.
* A foundation for **Undergraduate Theses (TCC)** or academic research projects.
* An experimental prototype for studies in **Human–Computer Interaction**.
* A testbed for multimodal conversational agent research.

---

## Ethical Considerations

The use of language models and voice-based systems must adhere to ethical principles, including:

* Responsible use of data and AI technologies.
* Transparency regarding system capabilities and limitations.
* Avoidance of inappropriate replacement of human interaction in sensitive contexts.
* Compliance with institutional and academic ethical guidelines.

---

## Authorship and Institution

Project developed within the academic context of **Universidade Paulista (UNIP)**.

**Author:** Valeria Kiohara
**Field:** Artificial Intelligence, Robotics, and Intelligent Systems

---

## License

This project is intended **exclusively for academic and educational purposes**.

Permission is granted to use, study, and modify the source code for **non-commercial and academic use**, provided that proper credit is given to the author and to Universidade Paulista (UNIP).

Commercial use, redistribution without attribution, or use in proprietary systems is **not permitted** without prior written authorization from the author.

The software is provided "as is", without warranty of any kind, express or implied.
