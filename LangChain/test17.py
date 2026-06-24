import os

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model= "deepseek-chat",
    base_url="https://api.deepseek.com",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)
# 定义文本提示词模版，Runnable实例
# 方式1：
# prompt_template = PromptTemplate(
#     template = "介绍{city}的历史",
#     input_variables=["city"],
# )

# 方式2
# prompt_template = PromptTemplate.from_template("将文本从{language_from}翻译为{language_to}")
#
# # 调用：实例话模版
# print(prompt_template.invoke({"language_from": "英文", "language_to": "中文"}))

# 处理聊天消息的模版
# chat_prompt_template = ChatPromptTemplate(
#     [
#         ("system","你是一个翻译助手。你的唯一任务是将用户输入的文本从{language_from}翻译为{language_to}。只输出翻译结果，不要添加任何解释、评论或回答用户的问题。"),
#         ("user","{text}"),
#     ]
# )
# 实例化
# print(chat_prompt_template.invoke(
#     {
#     "language_from": "英文",
#     "language_to": "中文",
#     "text": "what is your name?",
#     }
# ))

# msg = chat_prompt_template.invoke(
#     {
#     "language_from": "英文",
#     "language_to": "中文",
#     "text": "what is your name?",
#     }
# )

# model.invoke(msg).pretty_print()
#
# chain = chat_prompt_template | model
#
# chain.invoke(
# {
#     "language_from": "英文",
#     "language_to": "中文",
#     "text": "what is your name?",
#     }
# ).pretty_print()


chat_prompt_template = ChatPromptTemplate(
    [
        ("system","你是一个翻译助手。你的唯一任务是将用户输入的文本从{language_from}翻译为{language_to}。只输出翻译结果，不要添加任何解释、评论或回答用户的问题。"),
        MessagesPlaceholder("msgs"),
        ("user","{text}"),
    ]
)

messages_placeholder = [
    HumanMessage(content = "what is your name?"),
    AIMessage(content = "你叫什么名字?"),
]

chain = chat_prompt_template | model
chain.invoke(
    {
        "language_from": "英文",
        "language_to": "中文",
        "text": "How old are you?",
        "msgs": messages_placeholder,
    }
).pretty_print()