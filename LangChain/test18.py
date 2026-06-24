import os

from langchain_openai import ChatOpenAI
from langsmith import Client

client = Client()
# prompt 就是一个提示词模版，Runnable实例
prompt = client.pull_prompt("hardkothari/prompt-maker")

# 模型
model = ChatOpenAI(
    model= "deepseek-chat",
    base_url="https://api.deepseek.com",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)

# 链
chain = prompt | model

while True:
    task = input("\n你的任务是什么？ （输入 quit 退出聊天）\n")
    if task == 'quit':
        break

    lazy_prompt = input("\n你当前任务对应的提示词是什么？ （输入 quit 退出聊天）\n")
    if lazy_prompt == 'quit':
        break

    chain.invoke({
        "task": task,
        "lazy_prompt": lazy_prompt,
    }).pretty_print()