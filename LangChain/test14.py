import os

from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="deepseek-chat",
    base_url="https://api.deepseek.com",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    request_timeout=30,
    tiktoken_model_name="gpt-3.5-turbo",  # 用 gpt-3.5 的 tiktoken 编码，解决 deepseek-chat 不被识别的问题
)

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, trim_messages

#历史消息列表——个人介绍多轮对话
messages = [
    SystemMessage(content="你是一个友好的AI助手，请用中文回答所有问题。"),
    HumanMessage(content="你好！我想让你帮我记录一些关于我的个人信息。"),
    AIMessage(content="你好！当然可以，请告诉我你想让我记住哪些信息呢？"),
    HumanMessage(content="我叫张伟，今年28岁，目前在上海工作。"),
    AIMessage(content="记住了！张伟，28岁，在上海工作。请继续说。"),
    HumanMessage(content="我是一名后端开发工程师，主要用Python和Go。"),
    AIMessage(content="了解了，你是一名后端开发，技术栈是Python和Go。继续吧。"),
    HumanMessage(content="我的爱好是跑步和打篮球，周末经常去健身房。"),
    AIMessage(content="跑步、篮球、健身，你的业余生活很丰富啊！还有其他想告诉我的吗？"),
    HumanMessage(content="我养了一只猫叫豆豆，是一只橘猫。"),
    AIMessage(content="豆豆，橘猫——据说橘猫都很能吃，豆豆也是吗？"),
    HumanMessage(content="是的，豆豆特别能吃，现在已经快10斤了。"),
    AIMessage(content="哈哈，果然是典型的橘猫！还有别的要补充的吗？"),
    HumanMessage(content="你知道我是谁吗"),

]

# trim
# 使用 trim_message 减少发送给模型的消息数量
# trimer = trim_messages(
#     max_tokens = 1000,        # 修剪消息的最大令牌数，根据你想要的谈话长度来调整
#     strategy = "last",      # 修剪策略：last-保留最后的消息 first-保留最早的消息
#     token_counter=model,    # 传入一个函数或一个语言模型（因为语言模型有消息令牌计数方法）
#     include_system = True,  # 始终保留初始系统消息
#     allow_partial = False,  # 是否允许拆分消息的内容
#     start_on = "human",     # 确保我们的第一条消息（不包括系统消息）时钟是特定类型，可以进行指定
# )

trimer = trim_messages(
    max_tokens = 6,        # 修剪消息的最大令牌数，根据你想要的谈话长度来调整
    strategy = "last",      # 修剪策略：last-保留最后的消息 first-保留最早的消息
    token_counter=len,    # 传入一个函数或一个语言模型（因为语言模型有消息令牌计数方法）
    include_system = True,  # 始终保留初始系统消息
    allow_partial = False,  # 是否允许拆分消息的内容
    start_on = "human",     # 确保我们的第一条消息（不包括系统消息）时钟是特定类型，可以进行指定
)

chain = trimer | model
print(chain.invoke(messages))