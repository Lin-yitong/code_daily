import os
import warnings
from typing import List, TypedDict, Annotated, Union

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.utils.function_calling import tool_example_to_messages
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from pydantic.json_schema import PydanticJsonSchemaWarning

warnings.filterwarnings("ignore", category=PydanticJsonSchemaWarning)

model = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

# 1. 定义结构化输出
class Person(BaseModel):
    """一个人的信息"""
    name: str = Field(description="姓名"),
    hair_color: str = Field(description="头发颜色"),
    skin_color: str = Field(description="肤色"),
    height_in_meters: str = Field(description="身高（单位：米）"),

class Data(BaseModel):
    """人员列表信息"""
    people: List[Person] = Field(description="人员列表")

#2. 定义示例（不是Message）
examples = [
    (
        "海洋是广阔的、蓝色的。它有两万英尺多高",
        Data(people=[]),
    ),
    (
        "小明在跳舞，1米78的身高看起来很灵活",
        Data(people=[
            Person(name='小明',hair_color='None',skin_color='None',height_in_meters='1.78'),
        ])
    )
]

# 3. 定义提示词模版
prompt_template = ChatPromptTemplate(
    [
        SystemMessage(content="你是一个提取信息的专家，只从文本提取相关信息。如果您不知道要提取的属性值，属性值返回null"),
        MessagesPlaceholder("example_messages"),
        ("user","{new_message}")
    ]
)

# 4. 将示例转化为Message
#[[HumanMessage(content='海洋是广阔的、蓝色的。它有两万英尺多高', additional_kwargs={}, response_metadata={}),
# AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'b16512f6-6edc-4605-816a-68a95dd1007b', 'type': 'function', 'function': {'name': 'Data', 'arguments': '{"people":[]}'}}]}, response_metadata={}, tool_calls=[{'name': 'Data', 'args': {'people': []}, 'id': 'b16512f6-6edc-4605-816a-68a95dd1007b', 'type': 'tool_call'}], invalid_tool_calls=[]),
# ToolMessage(content='You have correctly called this tool.', tool_call_id='b16512f6-6edc-4605-816a-68a95dd1007b'),
# AIMessage(content='未检测到人', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])],

# [HumanMessage(content='小明在跳舞，1米78的身高看起来很灵活', additional_kwargs={}, response_metadata={}),
# AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'e88d119a-6511-438d-abc5-9d4d714dc91b', 'type': 'function', 'function': {'name': 'Data', 'arguments': '{"people":[{"name":"小明","hair_color":"None","skin_color":"None","height_in_meters":"1.78"}]}'}}]}, response_metadata={}, tool_calls=[{'name': 'Data', 'args': {'people': [{'name': '小明', 'hair_color': 'None', 'skin_color': 'None', 'height_in_meters': '1.78'}]}, 'id': 'e88d119a-6511-438d-abc5-9d4d714dc91b', 'type': 'tool_call'}], invalid_tool_calls=[]),
# ToolMessage(content='You have correctly called this tool.', tool_call_id='e88d119a-6511-438d-abc5-9d4d714dc91b'),
# AIMessage(content='检测到人', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])]]
example_messages = []
for txt,tool_call in examples:
    if tool_call.people:
        ai_response = "检测到人"
    else:
        ai_response = "未检测到人"
    example_messages.extend(tool_example_to_messages(
        txt, # 示例输出
        [tool_call], # 工具(Data(people = [])准确的参考标准)
        ai_response=ai_response,
    ))
# print(example_messages)

# 5. 定义结构化模型
model_with_structured = model.with_structured_output(schema=Data, method="function_calling")

# 6. 定义链
chain = prompt_template | model_with_structured
print(chain.invoke(
    {
    "example_messages": example_messages,
    "new_message": "张三有一头黑色的头发，皮肤偏黄，身高1.75米。",

    }
))

# messages = [
#     SystemMessage(content="你是一个提取信息的专家，只从文本提取相关信息。如果您不知道要提取的属性值，属性值返回null"),
#     HumanMessage(content="张三有一头黑色的头发，皮肤偏黄，身高1.75米。李四是金色头发，白皮肤，身高1.82米。"),
# ]
#
# result = model_with_structured.invoke(messages)
# print(result)