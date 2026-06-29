from langchain_redis import RedisConfig, RedisVectorStore
from langchain_siliconflow import SiliconFlowEmbeddings

# 嵌入模型
embeddings = SiliconFlowEmbeddings(
    model="BAAI/bge-large-zh-v1.5",
    api_key="sk-jwnepuqgavzxtfkbqqapnalxtfzmlhvvpimwrbwrmnsjlvvy",
    base_url="https://api.siliconflow.cn",
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