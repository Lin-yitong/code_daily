import os
from langchain_chroma import Chroma
from langchain_core.example_selectors import LengthBasedExampleSelector, SemanticSimilarityExampleSelector, \
    MaxMarginalRelevanceExampleSelector
from langchain_community.example_selectors import NGramOverlapExampleSelector
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_siliconflow import SiliconFlowEmbeddings

# 反义词实例集合
# examples = [
#     {"input":"happy","output":"sad"},
#     {"input":"big","output":"small"},
#     {"input":"fast","output":"slow"},
#     {"input":"energetic","output":"lethargic"},
#     {"input":"light","output":"dark"},
# ]

# 示例模版(文字)
example_prompt = PromptTemplate.from_template("Input:{input}\nOutput:{output}")

# 示例选择器(长度)
# example_selector = LengthBasedExampleSelector(
#     examples=examples,
#     example_prompt=example_prompt,
#     max_length=25, # 格式化实例的最大长度
# )

# 示例选择器（语义相似性）
embeddings = SiliconFlowEmbeddings(
    model="BAAI/bge-large-zh-v1.5",
    api_key="sk-jwnepuqgavzxtfkbqqapnalxtfzmlhvvpimwrbwrmnsjlvvy",
    base_url="https://api.siliconflow.cn",
)
# example_selector = SemanticSimilarityExampleSelector.from_examples(
#     examples,   # 示例集
#     embeddings, # 使用嵌入模型的能力度量语义
#     Chroma,     # 存储向量：向量数据库
#     k=2,  # 选取最相似的 k 个示例
# )

# 示例选择器（MMR）
# example_selector = MaxMarginalRelevanceExampleSelector.from_examples(
#     examples,
#     embeddings,
#     Chroma, #
#     k=2,  # 选取最相似的 k 个示例
# )

examples = [
    {"input":"See Spot run.","output":"看见Spot跑。"},
    {"input":"My dog barks.","output":"我的狗叫。"},
    {"input":"Spot can run.","output":"Spot可以跑。"},
]

# 示例选择器（NGram）
example_selector = NGramOverlapExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    threshold=1.0,  # NGram 重叠阈值，-1.0 表示不做过滤，0.0选择只与输入重叠，大于1.0则排除所有示例
)

# 少样本模版
# 转换 Meesage
few_shot_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="给出每个输入的中文翻译：",
    suffix="Input:{adjective}\nOutput:",
    input_variables=["adjective"],
)

print(few_shot_prompt.invoke({
    "adjective": "Spot can run fast.",
}).to_messages())

# few_shot_prompt = FewShotPromptTemplate(
#     example_selector=example_selector,
#     example_prompt=example_prompt,
#     prefix="给出每个输入的反义词：",
#     suffix="Input:{adjective}\nOutput:",
#     input_variables=["adjective"],
# )

# print(few_shot_prompt.invoke({
#     "adjective": "funny",
# }).to_messages()[0].content)