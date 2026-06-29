from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

# 定义嵌入模型
embeddings = OpenAIEmbeddings(
    model = "text-embedding-3-large"
)

# 将query转换成向量表示
query_vector = embeddings.embed_query("你好")
print(f"text-embedding-3-large 向量维度: {len(query_vector)}")
print(f"向量前五个数值: {query_vector[:5]}")

# single模式 只生成一个大文档
loder = UnstructuredMarkdownLoader("../Docs/markdown/自然资源主题新媒体科普宣传的实践与探索.md")
# Document列表
data = loder.load()

# tiktoken 分词器
text_spliter = CharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k-base",
    chunk_size=400,
    chunk_overlap=50,
)

# 文档列表
docs = text_spliter.split_documents(data)

# 将文档列表表示为向量
# 参数: text: list[str]
texts = [doc.page_content for doc in docs]
docs_vector = embeddings.embed_document(texts)

print(f"文档数量:{len(docs)},转换的向量列表数量：{len(docs_vector)}")
print(f"第一个文档向量维度: {len(docs_vector[0])}")
print(f"第一个文档向量前五个值：{docs_vector[0][:5]}")
