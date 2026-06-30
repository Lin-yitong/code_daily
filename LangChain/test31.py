from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_redis import RedisConfig, RedisVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from redisvl.query.filter import Tag, Num

# 嵌入模型（本地）
embeddings = HuggingFaceEmbeddings(
    model_name="F:/AI/ai-large-model-learning/models/BAAI/bge-small-zh-v1.5",
)

# Redis 配置
config = RedisConfig(
    index_name = "qa",
    redis_url = "redis://127.0.0.1:6379",
    metadata_schema=[
        {"name":"category","type":"tag"},   # 添加索引字段：分类
        {"name":"num","type":"numeric"},
    ]
)

# 初始化 Redis 向量存储实例
vector_store = RedisVectorStore(
    embeddings = embeddings,
    config = config,
)

# single模式 只生成一个大文档
loder = UnstructuredMarkdownLoader("../Docs/markdown/自然资源主题新媒体科普宣传的实践与探索.md")
# Document列表
data = loder.load()

# tiktoken 分词器
text_spliter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base",
    chunk_size=400,
    chunk_overlap=50,
)

# 文档列表
docs = text_spliter.split_documents(data)
for i,doc in enumerate(docs,start=1):
    doc.metadata["category"] =  "QA"
    doc.metadata["num"] = i

# 添加文档（编制索引）
# ids = vector_store.add_documents(docs)
# print(f"编制了{len(ids)}个索引")
# print(f"前三个索引是{ids[:3]}")

# 查
print(vector_store.get_by_ids(["01KWB5YCZ3CQ2JJ8AX8QHA2G9C"]))

# 删除
# vector_store.delete(["01KWB5YCZ3CQ2JJ8AX8QHA2G9C"])
# print(vector_store.get_by_ids(["01KWB5YCZ3CQ2JJ8AX8QHA2G9C"]))

# 批量删除
# vector_store.index.drop_keys(["qa:01KWB5YCZ3CQ2JJ8AX8QHA2G9C"])

# 全量删除（连带索引结构全部删除）
# vector_store.index.delete(drop=True)

# 检索
# search_doc = vector_store.similarity_search(query="阅读",k=2)
#结果打分
# search_doc_results = vector_store.similarity_search(query="<UNK>",k=2)

# 过滤条件
filter_condition = (Tag("category") == "QA") & (Num("num")>5)
# search_doc= vector_store.similarity_search_with_score(query="阅读",k=2,filter_condition=filter_condition)
#
# for doc,score in search_doc:
#     print( "*" * 30)
#     print(f"文档分数: {score}")
#     print(f"文档内容: {doc.page_content}")
#     print(f"文档元数据: {doc.metadata}")

# MMR搜索：基于语义搜索，先筛选出一批文档 ，然后进行重排序输出
search_docs = vector_store.max_marginal_relevance_search(
    query="阅读",
    k=2,
    filter_condition=filter_condition,
    fetch_k=10,
)

for doc in search_docs:
    print( "*" * 30)
    print(f"文档内容: {doc.page_content}")
    print(f"文档元数据: {doc.metadata}")

