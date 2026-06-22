import os

from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model= "deepseek-chat", base_url="https://api.deepseek.com", api_key=os.getenv("DEEPSEEK_API_KEY"))

# model.invoke("我是小明，你好").pretty_print()
# model.invoke("你知道我是谁吗？").pretty_print()

# messages = [
#     HumanMessage(content="我是小明，你好"),
#     AIMessage(content="小明，你好"),
#     HumanMessage(content="你知道我是谁吗"),
# ]
#
# model.invoke(messages).pretty_print()


store = {}
# 根据会话 id 查询会话里面的消息列表
def get_session_history(session_id: str) ->BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# 包装model，让model具备存储历史消息的能力
with_history_message_model = RunnableWithMessageHistory(model, get_session_history)

# model : Runnable实例
# invoke : config 配置 Runnable实例
config ={"configurable":{"session_id" : "1"}}

with_history_message_model.invoke(
    [HumanMessage(content="我是小明，你好！")],
    config = config,
).pretty_print()

with_history_message_model.invoke(
    [HumanMessage(content="你知道我是谁吗")],
    config = config,
).pretty_print()



