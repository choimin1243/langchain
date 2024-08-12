import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(api_key=OPENAI_API_KEY,model_name="gpt-3.5-turbo-0125")

prompt=ChatPromptTemplate(
    [("system","당신은 천문학전문가입니다."),("user","{input}")]
)


print(prompt)


prompt_text=prompt.format(input="지구의 자전주기는 얼마인가요?")


response=llm.invoke(prompt_text)
output_parser=StrOutputParser()


chain=prompt|llm|output_parser

response=chain.invoke({"input":"지구의 자전주기는 얼마인가요?"})

print(response)