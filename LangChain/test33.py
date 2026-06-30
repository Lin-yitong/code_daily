from typing import List

from langchain_core.documents import Document
from langchain_core.runnables import chain
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_redis import RedisConfig, RedisVectorStore

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

# 检索器依赖向量库（Runnable）
# retriever = vector_store.as_retriever(search_kwargs={"k":2})

# 使用@chain, 定义检索器函数，当做具有Runnable的"检索器"使用-更具有灵活性
@chain
def retriever(query:str) -> List[Document]:
    return vector_store.similarity_search(query = query,k=2)

search_docs = retriever.invoke("阅读")
for doc in search_docs:
    print("*" * 30)
    print(doc.page_content)