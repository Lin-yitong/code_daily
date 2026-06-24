import os

from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model= "deepseek-chat",
    base_url="https://api.deepseek.com",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)
# 文本提示词模版
example_prompt = PromptTemplate.from_template("Question:{question}\n{answer}")

# 创建示例集合 —— 每个示例的 answer 展示完整思维链
examples = [
    {
        "question": "《教父》和《星球大战》的导演是否来自同一个国家？",
        "answer": """
            是否需要后续问题：是
            后续问题1：《教父》的导演是谁？
            中间答案1：《教父》的导演是弗朗西斯·福特·科波拉。
            后续问题2：《星球大战》的导演是谁？
            中间答案2：《星球大战》的导演是乔治·卢卡斯。
            后续问题3：弗朗西斯·福特·科波拉和乔治·卢卡斯分别来自哪个国家？
            中间答案3：科波拉来自美国，卢卡斯也来自美国。
            最终答案：是，《教父》和《星球大战》的导演都来自美国，他们来自同一个国家。
    """,},
    {
        "question": "如果今天是星期三，100天后是星期几？",
        "answer": """
            是否需要后续问题：是
            后续问题1：一周有几天？
            中间答案1：一周有7天。
            后续问题2：100除以7的商和余数分别是多少？
            中间答案2：100÷7=14余2，即100天后相当于过了14个完整星期再加2天。
            后续问题3：星期三往后推2天是星期几？
            中间答案3：星期三→星期四(1天)→星期五(2天)。
            最终答案：100天后是星期五。
    """,},
    {
        "question": "水的沸点在珠穆朗玛峰山顶大约是多少度？",
        "answer": """
            是否需要后续问题：是
            后续问题1：珠穆朗玛峰山顶的海拔高度是多少？
            中间答案1：珠穆朗玛峰山顶海拔约8848米。
            后续问题2：海拔升高对水的沸点有什么影响？
            中间答案2：海拔越高，气压越低，水的沸点越低。大约每升高300米，沸点下降约1°C。
            后续问题3：在8848米处，沸点大约下降了多少度？
            中间答案3：8848÷300×1≈29.5°C，因此沸点约为100-29.5=70.5°C。
            最终答案：在珠穆朗玛峰山顶，水的沸点大约为70-71°C。
    """,},
]

# FewShotPromptTemplate：将示例格式化后拼接到 prompt 中
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,    # PromptTemplate，用于格式化单个示例
    suffix="Question:{input}",        # suffix 放在示例之后，承载用户实际输入
    input_variables=["input"],        # 输入变量列表
    prefix="以下是使用思维链方式回答问题的示例，请仿照此格式回答用户的问题：\n",  # prefix 放在示例之前，给出指令
)

# 打印拼接后的完整 prompt
# print(few_shot_prompt.invoke({"input": "《教父》和《星球大战》的导演是否来自同一个国家？"}))
# print("\n" + "="*50 + "\n")

chain = few_shot_prompt | model
chain.invoke({"input": "《教父》和《星球大战》的导演是否来自同一个民族？"}).pretty_print()


