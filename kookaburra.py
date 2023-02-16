from langchain.llms import OpenAI


def get_llm() -> OpenAI:
    return OpenAI(temperature=0.9)
