import os

from langchain_core.output_parsers import PydanticOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

# 定义聊天模型
model = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

# Pydantic对象
class Joke(BaseModel):
    """给用户讲的一个笑话"""
    setup: str = Field(description="这个笑话的开头"),
    punchline: str = Field(description="这个笑话的妙语"),
    rating: int = Field(description="从1-10分，给这个笑话打分")

# 定义解析器
# parser = PydanticOutputParser(pydantic_object=Joke)
# print(parser.get_format_instructions())

# Json Schema
parser = JsonOutputParser(pydantic_object=Joke)

# 提示词模版
prompt = PromptTemplate(
    template="回复用户问题。\n返回结构说明:{fromat_instructions}\n用户问题:{query}\n",
    partial_variables={"fromat_instructions": {parser.get_format_instructions()}}, # 将返回的结构作为提示词发送给大模型
    input_variables=["query"]
)

# print(prompt.invoke({"query": "讲一个关于跳舞的笑话"}))

# 定义链
chain = prompt | model | parser
print(chain.invoke({"query": "讲一个关于跳舞的笑话"}))