# 🤖 UNIP Face LLM

Assistente de voz com rosto animado usando Vosk, Gemini e Piper TTS.

## Execução
```bash
python src/unip_face/main.py


# UNIP Face LLM

## Resumo

O **UNIP Face LLM** é um projeto acadêmico-experimental desenvolvido no contexto da Universidade Paulista (UNIP), com o objetivo de integrar **Modelos de Linguagem de Grande Escala (LLMs)** a uma interface interativa multimodal, combinando **Processamento de Linguagem Natural (PLN)**, **Síntese de Voz (Text-to-Speech – TTS)** e **interação visual**.

O projeto explora conceitos de Inteligência Artificial Aplicada, Sistemas Conversacionais e Arquiteturas Modulares, servindo como base para estudos, prototipação e futuras extensões em ambientes acadêmicos e de pesquisa.

---

## Objetivos do Projeto

Os principais objetivos do UNIP Face LLM são:

* Investigar a aplicação prática de **LLMs** em sistemas interativos.
* Integrar modelos de linguagem com **síntese de voz offline** e online.
* Desenvolver uma arquitetura modular, extensível e documentada.
* Servir como **projeto acadêmico demonstrativo** para disciplinas relacionadas à Inteligência Artificial, Robótica e Sistemas Inteligentes.

---

## Escopo e Funcionalidades

Atualmente, o projeto contempla:

* Integração com APIs de LLM (modo online).
* Síntese de voz utilizando **Piper TTS** (execução local/offline).
* Estrutura de projeto organizada em módulos.
* Suporte a variáveis de ambiente para configuração segura.
* Base para interface visual interativa (face/avatar).

Funcionalidades futuras podem incluir:

* Reconhecimento automático de fala (ASR).
* Integração com sistemas robóticos ou agentes físicos.
* Avaliação de desempenho e métricas acadêmicas.

---

## Estrutura do Projeto

A organização do repositório segue boas práticas de engenharia de software:

```text
unip-face-llm/
├── assets/           # Recursos visuais, áudios e mídias
├── docs/             # Documentação técnica e acadêmica
├── src/              # Código-fonte principal do projeto
├── .env.example      # Exemplo de variáveis de ambiente
├── .gitignore        # Arquivos e pastas ignorados pelo Git
├── README.md         # Documentação principal do projeto
└── requirements.txt  # Dependências do projeto
```

---

## Requisitos do Sistema

* Python 3.10 ou superior
* Ambiente Linux (recomendado)
* Dependências listadas em `requirements.txt`

Instalação das dependências:

```bash
pip install -r requirements.txt
```

---

## Configuração

As configurações sensíveis (como chaves de API) devem ser definidas por meio de variáveis de ambiente.

1. Copie o arquivo de exemplo:

```bash
cp .env.example .env
```

2. Preencha os valores conforme o ambiente de execução.

---

## Metodologia e Abordagem Técnica

O projeto adota uma abordagem modular, permitindo:

* Separação clara entre lógica de negócio, integração com LLMs e interface.
* Facilidade de manutenção e extensão.
* Reprodutibilidade em contextos acadêmicos.

A escolha por ferramentas open-source visa estimular o aprendizado, a análise crítica e a adaptação do sistema a diferentes cenários de pesquisa.

---

## Aplicações Acadêmicas

O UNIP Face LLM pode ser utilizado como:

* Projeto de apoio em disciplinas de Inteligência Artificial.
* Base para Trabalhos de Conclusão de Curso (TCC).
* Protótipo experimental para estudos em interação humano-computador.

---

## Considerações Éticas

O uso de modelos de linguagem e sistemas de voz deve respeitar princípios éticos, incluindo:

* Uso responsável de dados.
* Transparência quanto às capacidades e limitações do sistema.
* Não substituição indevida de interações humanas em contextos sensíveis.

---

## Autoria e Instituição

Projeto desenvolvido no contexto acadêmico da **Universidade Paulista (UNIP)**.

Autoria: **Valeria Kiohara**
Curso/Área: Inteligência Artificial, Robótica e Sistemas Inteligentes

---

## Licença

Este projeto é destinado a fins **acadêmicos e educacionais**. A licença específica pode ser definida conforme a necessidade institucional.

```
