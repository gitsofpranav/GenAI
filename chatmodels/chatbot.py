from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain.messages import SystemMessage, HumanMessage, AIMessage



model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0,
    max_tokens=50
)

message = [
   SystemMessage("You are a poetry expert"),
]
print("------------- welcome type 0 to exit the appliction --------")
while True:

   prompt = input("You : ")
   message.append(HumanMessage(prompt))

   if(prompt == "0") :
    break

   response = model.invoke(message)
   message.append(AIMessage(response.content))
   print("Bot : ",response.content)

print(message)   