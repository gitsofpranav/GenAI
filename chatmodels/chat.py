from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model



model = init_chat_model("google_genai:gemini-3.1-flash-lite")


response = model.invoke("how to get hired in 2026 for SDE role")
print(response.content)