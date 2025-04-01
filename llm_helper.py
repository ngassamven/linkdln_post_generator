from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="mistral-saba-24b")

if __name__ == "__main__":
    query = "Two most important ingredients in samosa are"  # Assurez-vous que query est une chaîne de caractères
    # Pas besoin de `encode('utf-8')` ici, car `llm.invoke()` prend déjà des chaînes de caractères en entrée.
    response = llm.invoke(query)  # Envoie directement la chaîne
    print(response.content)
