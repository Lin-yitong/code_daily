import os

from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage


# 1. 基本用法
# langchain 封装了更上层的方法，让我们初始化模型
# deepseek_model = init_chat_model(model = "deepseek-v4-flash")
# print(deepseek_model.invoke("你是谁").content)
#
#
# # 2. 定义可配置的模型
# config_model = init_chat_model(temperature=0.3)
# messages = [
#     SystemMessage(content="请补全一段故事，10个字以内："),
#     HumanMessage(content="一只猫正在__?"),
# ]
# print(config_model.invoke(input = messages,config={"configurable":{"model":"deepseek-v4-flash"}}).content)

# 3. 可配置的模型（默认参数）
# 原本输出
# 精简输出
model = init_chat_model(
    model = "deepseek-chat",
    temperature=0.3,
    max_tokens=1024,
    configurable_fields=("max_tokens",),
    config_prefix="first",
)
messages = [
    SystemMessage(content="请补全一段故事，100个字以内："),
    HumanMessage(content="一只猫正在__?"),
]

result = model.invoke(
    input=messages,
    config={
        "configurable": {
            "first_max_tokens": 10,
        }
    })

print(result.content)
