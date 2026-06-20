import os

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI

# 1. 定义 DeepSeek 模型
# 从系统环境变量 DEEPSEEK_API_KEY 中读取密钥
model = ChatOpenAI(
    model="deepseek-v4-flash",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.comq",
    temperature= 0,
)

# 2. 定义消息
# 系统提示消息 SystemMessage 通常作为第一条消息传入
# 用户消息 HumanMessage
messages = [
    SystemMessage("请补全一段故事，10个字以内"),
    HumanMessage("一只猫正在__?"),
]

# 3. 调用大模型
# result = model.invoke(messages)
# print(result)

# 4. 定义输出解释器组件
parser = StrOutputParser()
# print(parser.invoke(result))

# 5. 定义链
chain = model | parser
# chain = RunnableSequence(first=model,last=parser)
# chain = model.pipe(parser)
print(chain.invoke(messages))
