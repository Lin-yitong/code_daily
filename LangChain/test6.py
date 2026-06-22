import os

from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from typing import Annotated

from langchain_openai import ChatOpenAI


@tool
def add(
        a: Annotated[int, "第一个整数"],
        b: Annotated[int, "第二个整数"],
) -> int:
    """两数相加"""
    return a + b

@tool
def multiply(
        a: Annotated[int, "第一个整数"],
        b: Annotated[int, "第二个整数"],
) -> int:
    """两数相乘"""
    return a * b

model = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

# 绑定工具
tools = [add, multiply]
# model_with_tools = model.bind_tools(tools=tools)
# 强制使用工具
model_with_tools = model.bind_tools(tools=tools,tool_choice="any")

# 调用工具---实际大模型是先选择工具再调用工具
# print(model_with_tools.invoke("2乘3等于多少？严格使用工具"))
# print(model_with_tools.invoke("你是谁"))

# ai_msg = model_with_tools.invoke("2乘3等于多少")
# print(multiply.invoke(ai_msg.tool_calls[0]))

# 定义消息列表，添加要传递给聊天模型的消息：Human_message,ai_message,tools_message,system_message
messages = [
    HumanMessage("2乘3等于几？5+5等于几")
]

ai_msg = model_with_tools.invoke(messages)
messages.append(ai_msg)  # AIMessage 必须在 ToolMessage 前面
print(ai_msg)

# 构造ToolMessage，并添加到消息队列里去
for tool_call in ai_msg.tool_calls:
    select_tool = {"add":add, "multiply":multiply}[tool_call["name"].lower()]
    tool_msg = select_tool.invoke(tool_call)
    messages.append(tool_msg)

print(messages)
print(model.invoke(messages).content)