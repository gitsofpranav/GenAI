from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-V4-Flash-0731"
    )

model = ChatHuggingFace(llm = llm)

response = model.invoke("why in 2026 the Tech industriy is not hiring frehser")
print(response.content)
