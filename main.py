from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

CAMINHO_DB ="db"

prompt_template="""Responda a perguntar do colaborador:{pergunta} 
com base nessas informações: {base_conhecimento}
Se você não encontrar a resposta, responda não sei te dizer isso
"""

def perguntar ():
    pergunta = input("Escreva sua dúvida")

    funcao_embedding = OpenAIEmbeddings()
    db = Chroma(persist_directory=CAMINHO_DB, embedding_function=funcao_embedding)

    resultados = db.similarity_search_with_relevance_scores(pergunta, k=4)
    if len(resultados) == 0 or resultados[0][1] < 0.7:
        print("Não conseguiu encontrar alguma informação relevante na base")
        return
    
    texto_resultados = []
    for resultado in resultados:
        texto= resultado[0].page_content
        texto_resultados.append(texto)

    base_conhecimento = "\n\n----\n\n".join(texto_resultados)

    prompt = ChatPromptTemplate.from_template(prompt_template)
    prompt= prompt.invoke({"pergunta}":pergunta, "base_conhecimento":base_conhecimento})
    

    modelo = ChatOpenAI()
    texto_resposta = modelo.invoke(prompt).content
    print("Resposta da IA:", texto_resposta)

perguntar()
