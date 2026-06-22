import os

from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model= "deepseek-chat",
    base_url="https://api.deepseek.com",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)

# 返回一个迭代器，产生的消息块
for chunk in model.stream("写一篇关于春天的作文，500字左右"):
    print(chunk.content,end='|',flush=True)