from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pinecone import Pinecone
# 创建Pinecone客户端
pc = Pinecone()
index_name = "qa"
if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=512,      # 维度，与 bge-small-zh-v1.5 输出维度一致
        metric="cosine",    # 度量方式，consine余弦相似度
        spec={
            "serverless": {
                "cloud": "aws",            # 亚马逊云
                "region": "us-east-1",     # 区域
            }
        },
    )

# 获取索引
index = pc.Index(index_name)
# 嵌入模型
embeddings = HuggingFaceEmbeddings(
    model_name="F:/AI/ai-large-model-learning/models/BAAI/bge-small-zh-v1.5",
)
# 定义 pinecone向量库
vector_store = PineconeVectorStore(
    embedding = embeddings,
    index = index,
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
ids = vector_store.add_documents(docs)
print(f"编制了{len(ids)}个索引")
print(f"前三个索引是{ids[:3]}")
