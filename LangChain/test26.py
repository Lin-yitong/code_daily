from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter

# single 模式, 只生成一个大文档
loader = UnstructuredMarkdownLoader("../docs/markdown/自然资源主题新媒体科普宣传的实践与探索.md")
# Doucument 列表
data = loader.load()

# 定义文本分割器
# text_spliter = CharacterTextSplitter(
#     separator="\n\n",       # 分割符，一般来说，有一个默认的分隔符优先级列表：["\n\n","\n"," "]
#     chunk_size=400,         # 块大小（参考标准，为了保证段落/句子完整，会超出此设定的大小）
#     chunk_overlap=50,       # 块重叠大小
#     length_function=len,    #测量字符长度的函数
#     is_separator_regex=False,#是否正则表达式描写分隔符
# )

# tiktoken 分词器
# text_spliter = CharacterTextSplitter.from_tiktoken_encoder(
#     encoding_name="cl100k_base",
#     chunk_size=400,
#     chunk_overlap=50,
# )

# 强制按照约定的块大小分割文本
# text_spliter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
#     encoding_name="cl100k_base",
#     chunk_size=400,
#     chunk_overlap=50,
# )

text_spliter = RecursiveCharacterTextSplitter(
    separator=["\n\n","\n"," "],  # 分割符，一般来说，有一个默认的分隔符优先级列表：["\n\n","\n"," "]
    chunk_size=400,         # 块大小（参考标准，为了保证段落/句子完整，会超出此设定的大小）
    chunk_overlap=50,       # 块重叠大小
    length_function=len,    #测量字符长度的函数
    is_separator_regex=False,#是否正则表达式描写分隔符
)



# 分割文档
documents = text_spliter.split_documents(data)
for doc in documents:
    print("*"*30)
    print(doc)
