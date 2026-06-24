import os

from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_openai import ChatOpenAI

# 案例：参数
examples = [
    {"text": "hi,what is your name?", "output": "你好，你叫什么名字?"},
    {"text": "hi,how old are you?", "output": "你好，你多大了?"},
]

# 与案例相关联的聊天消息模版
example_prompt = ChatPromptTemplate(
    [
        ("user","{text}"),
        ("ai","{output}"),
    ]
)

# 少样本聊天消息提示词模版
few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
)

# 最终提示词模版
chat_prompt_template = ChatPromptTemplate(
    [
        ("system",
         "你是一个翻译助手。你的唯一任务是将用户输入的文本从{language_from}翻译为{language_to}。只输出翻译结果，不要添加任何解释、评论或回答用户的问题。"),
        few_shot_prompt,
        ("user", "{text}"),
    ]
)

# SystemMessage(content='你是一个翻译助手。你的唯一任务是将用户输入的文本从英文翻译为中文。只输出翻译结果，不要添加任何解释、评论或回答用户的问题。', additional_kwargs={}, response_metadata={}),
# HumanMessage(content='hi,what is your name?', additional_kwargs={}, response_metadata={}),
# AIMessage(content='你好，你叫什么名字?', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]),
# HumanMessage(content='hi,how old are you?', additional_kwargs={}, response_metadata={}),
# AIMessage(content='你好，你多大了?', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]),
# HumanMessage(content='hi,what is your favourite food?', additional_kwargs={}, response_metadata={})
# print(chat_prompt_template.invoke({
#     "language_from": "英文",
#     "language_to": "中文",
#     "text": "hi,what is your favourite food?",
# }))

model = ChatOpenAI(
    model= "deepseek-chat",
    base_url="https://api.deepseek.com",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)

chain = chat_prompt_template | model
chain.invoke({
    "language_from": "英文",
    "language_to": "中文",
    "text": "hi,what is your favourite food?",
}).pretty_print()