from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str


parser = PydanticOutputParser(pydantic_object=Movie)


llm = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0
)


prompt = ChatPromptTemplate.from_messages([
    ("system", """
Extract movie Information from the paragraph.

{formate_instructions}
"""),
    ("human", "{paragraph}")
])


para = input("Give me the paragraph: ")

if para.strip():
    final_prompt = prompt.invoke({
        "paragraph": para,
        "formate_instructions": parser.get_format_instructions()
    })

    response = llm.invoke(final_prompt)

    print(response.content)
else:
    print("Please enter a paragraph.")