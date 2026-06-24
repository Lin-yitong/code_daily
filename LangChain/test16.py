import os

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, merge_message_runs
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model= "deepseek-chat",
    base_url="https://api.deepseek.com",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)

messages = [
    SystemMessage("你是一个聊天助手"),
    SystemMessage("你总是以笑话回应"),
    HumanMessage("为什么要使用LongChain"),
    HumanMessage("为什么要使用LongGraph"),
    AIMessage("因为当你试图让你的代码更有条理时，LongGraph会让你感到“节点”是一好主意！"),
    AIMessage("不过别担心，它不会分散你的注意力"),
    HumanMessage("选择LongChain还是LongGraph"),
]

merger = merge_message_runs()

chain = merger | model
chain.invoke(messages).pretty_print()