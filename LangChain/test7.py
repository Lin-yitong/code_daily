import os

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

# 定义模型
model = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

# 定义工具
tool = TavilySearch(max_results=4)

# 绑定工具
model_with_tool = model.bind_tools([tool])


# 定义消息
messages = [
    HumanMessage("厦门今天的天气怎么样")
]
ai_message = model_with_tool.invoke(messages)
messages.append(ai_message)

for tool_call in ai_message.tool_calls:
    tool_message = tool.invoke(tool_call)
    print("工具返回内容:", tool_message.content)
    messages.append(tool_message)

print(model.invoke(messages).content)

