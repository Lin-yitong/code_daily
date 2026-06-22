import os
from typing import List, TypedDict, Annotated, Union

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

model = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

# Pydantic对象来约束输出
class Joke(BaseModel):
    setup: str = Field(description="这个笑话的开头"),
    punchline: str = Field(description="这个笑话的妙语"),
    rating: int = Field(description="从1-10分，给这个笑话打分")

class Response(BaseModel):
    """用以对话的方式回应"""

    content: str = Field(description="用于对用户查询的会话响应")

class FinalResponse(BaseModel):
    """最终回复，选择合适的输出结构"""
    final_content: Union[Joke,Response]

model_with_structured=model.with_structured_output(FinalResponse,method="function_calling")
print(model_with_structured.invoke("给我讲一个关于小猪的笑话"))
print(model_with_structured.invoke("你是谁"))