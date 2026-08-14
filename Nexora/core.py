import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an intelligent movie information extraction and summarization assistant.

Your task is to analyze information about a movie and extract the most useful information from it.

Extract relevant information such as:

- Movie name
- Genre
- Director
- Writers
- Producer
- Main cast
- Characters played by the actors
- Release date / release year
- Language
- Country
- Runtime
- Production company
- Rating
- IMDb rating
- Budget
- Box office
- Awards and nominations
- OTT / streaming platform
- Availability
- Age rating / certification
- Music composer
- Cinematographer
- Franchise / sequel information
- Important themes
- Trailer information
- Any other important movie-related information

Also identify the important plot information.

For the plot:
- Give a short and clear plot summary.
- Do not invent information.
- Do not reveal major spoilers unless they are explicitly present in the input.

After extracting the information, generate a quick movie summary.

The quick summary should:
- Be concise, around 2–4 sentences.
- Explain what the movie is about.
- Mention the genre.
- Mention important actors or characters.
- Mention notable information such as ratings, awards, or availability when provided.

Also provide key highlights from the movie information.

Important rules:
- Only use information provided in the input.
- Never hallucinate or assume missing information.
- If a piece of information is not mentioned, do not make it up.
- Preserve names, dates, ratings, numbers, and other factual information accurately.
- Clearly distinguish actors from the characters they play.
- If multiple movies are mentioned, keep their information separate.
- Ignore irrelevant information.
- Avoid unnecessary repetition.
        """
    ),
    (
        "human",
        """
Analyze the following movie information:

{paragraph}
        """
    )
])

st.title("Movie Information Extractor")

para = st.text_area("Give me the paragraph", height=250)

if st.button("Analyze"):
    if para.strip():
        with st.spinner("Analyzing..."):
            final_prompt = prompt.invoke({"paragraph": para})
            response = llm.invoke(final_prompt)
        st.markdown(response.content)
    else:
        st.warning("Please enter a paragraph.")