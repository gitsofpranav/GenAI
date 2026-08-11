from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI



model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0,
    max_tokens=50
)

response = model.invoke("how to get hired in 2026 for SDE role")

print(response.content)