from typing import Tuple, List

from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


# 方式一
# def add(a:int,b:int):
#     """两数相加"""
#     return a+b
# add_tool = StructuredTool.from_function(func=add)

# 方式二
# class AddInput(BaseModel):
#     a:int = Field(description="第一个整数")
#     b:int = Field(description="第二个整数")
#
# def add(a:int, b:int):
#     return a + b
#
# add_tool = StructuredTool.from_function(
#     func=add,
#     name="ADD",     # 工具名
#     description="两数相加", # 工具描述
#     add_input=AddInput, #工具参数
# )

# print(add_tool.invoke({"a":2,"b":3}))


# 方式三：看到过程
class AddInput(BaseModel):
    a: int = Field(description="第一个整数")
    b: int = Field(description="第二个整数")

def add(a: int, b: int)-> Tuple[str,List[int]]:
    nums = [a,b]
    content = f"{nums}相加的结果是{a+b}"
    return content,nums

add_tool = StructuredTool.from_function(
    func=add,
    name="Add",
    description="两数相加",
    args_schema=AddInput,
    response_format="content_and_artifact"
)

# 模拟大模型调用方式
print(add_tool.invoke(
    {
        "name":"Add",
        "args":{"a":1,"b":2},
        "type": "tool_call",    # 必填
        "id":   "111",          #必填
    }
))
