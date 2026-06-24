
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, filter_messages

messages = [
    SystemMessage(content="你是一个乐于助人的AI助手。", id="1"),
    HumanMessage(content="你好，请问今天能帮我做什么？", id="2"),
    AIMessage(content="你好！我可以帮你解答问题、编写代码、提供建议等。有什么需要帮忙的吗？", id="3"),
    HumanMessage(content="能给我解释一下什么是机器学习吗？", id="4"),
    AIMessage(content="机器学习是人工智能的一个分支，它让计算机能够从数据中学习规律，而不需要显式编程。主要有监督学习、无监督学习和强化学习三种类型。", id="5"),
    HumanMessage(content="监督学习和无监督学习有什么区别？", id="6"),
    AIMessage(content="监督学习使用带标签的数据进行训练，比如已知输入和对应输出的数据；而无监督学习使用未标注的数据，让模型自己去发现数据中的模式和结构。", id="7"),
]

# 按照类型进行筛选
# print(filter_messages(messages, include_types='human'))
# print(filter_messages(include_types='ai').invoke(messages))

# 按照id进行筛选
# print(filter_messages(messages, exclude_ids=["3"]))

# 按照id+类型进行筛选
print(filter_messages(messages, exclude_ids=["3"],include_types=["human","ai"]))
