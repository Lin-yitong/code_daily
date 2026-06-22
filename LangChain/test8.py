import os
from typing import List, TypedDict, Annotated

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

model = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

# Pydantic对象来约束输出
# class Joke(BaseModel):
#     setup: str = Field(description="这个笑话的开头"),
#     punchline: str = Field(description="这个笑话的妙语"),
#     rating: int = Field(description="从1-10分，给这个笑话打分"),
#
# class Data(BaseModel):
#     """获取关于笑话的数据列表"""
#     jokes : List[Joke]

# TypeDict--一般用于格式和内容检查
# class Joke(TypedDict):
#     setup: Annotated[str,...,"这个笑话的开头"]
#     punchline: Annotated[str,...,"这个笑话的妙语"]
#     rating:  Annotated[int,...,"从1-10分，给这个笑话打分"]

# JSON Schema
json_schema = {
    "title": "Joke",
    "description": "一个笑话",
    "type": "object",
    "properties": {
        "setup": {"type": "string", "description": "这个笑话的开头"},
        "punchline": {"type": "string", "description": "这个笑话的妙语"},
        "rating": {"type": "integer", "description": "从1-10分，给这个笑话打分"},
    },
    "required": ["setup", "punchline", "rating"],
}

# model_with_structured = model.with_structured_output(Joke, method="function_calling")
# print(model_with_structured.invoke("讲一个关于唱歌的笑话"))

# model_with_structured = model.with_structured_output(Data, method="function_calling")
# print(model_with_structured.invoke("分别讲一个唱歌和跳舞的笑话"))
#
# model_with_structured = model.with_structured_output(Joke, method="function_calling",include_raw=True)
# print(model_with_structured.invoke("分别讲一个跳舞的笑话"))


model_with_structured = model.with_structured_output(json_schema, method="function_calling")
print(model_with_structured.invoke("讲一个跳舞的笑话"))