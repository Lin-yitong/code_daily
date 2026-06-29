from langchain_core.vectorstores import InMemoryVectorStore
from langchain_siliconflow import SiliconFlowEmbeddings
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

embeddings = SiliconFlowEmbeddings(
    model="BAAI/bge-large-zh-v1.5",
    api_key="sk-jwnepuqgavzxtfkbqqapnalxtfzmlhvvpimwrbwrmnsjlvvy",
    base_url="https://api.siliconflow.cn",
)

# 内存向量存储
vector_store = InMemoryVectorStore(embedding= embeddings)

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

# 存储文档到内存向量存储中
# add_documents: 将要存储的文档列表进行编排索引
ids = vector_store.add_documents(docs)
print(f"共有{len(docs)}个文档，编排了{len(ids)}个索引")
print(f"前三个文档的索引：{ids[:3]}")

# 根据索引获取文档
doc_2 = vector_store.get_by_ids(ids[:2])
print(doc_2)

# 删除文档
vector_store.delete(ids[:2])

doc_3 = vector_store.get_by_ids(ids[:3])
print(doc_3)
