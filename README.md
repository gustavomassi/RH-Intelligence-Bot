# RH-Intelligence-Bot 🤖

Chatbot inteligente desenvolvido com arquitetura **RAG (Retrieval-Augmented Generation)** para consulta de documentos corporativos em PDF.

O sistema utiliza busca semântica para responder perguntas com base em documentos internos, como:

* acordo coletivo
* diretrizes corporativas
* férias
* normas internas
* políticas administrativas

## 🚀 Tecnologias utilizadas

* Python
* LangChain
* ChromaDB
* Retrieval-Augmented Generation (RAG)
* Processamento de PDF

## ⚙️ Como funciona

1. O documento PDF é carregado
2. O conteúdo é dividido em chunks
3. Os embeddings são gerados
4. O banco vetorial é criado
5. O chatbot consulta as informações e responde com contexto

## 📂 Estrutura do projeto

```bash
main.py        # execução principal do chatbot
criar_db.py    # geração do banco vetorial
.gitignore     # arquivos ignorados no Git
```

## 🎯 Objetivo

Facilitar o acesso rápido e inteligente a informações corporativas sem necessidade de busca manual em documentos extensos.

## 💡 Exemplo de perguntas

* Quantos dias de férias posso vender?
* O que diz o acordo coletivo sobre afastamento?
* Como funciona o o processo interno de solicitação?

📌 Autor

Gustavo Massi
