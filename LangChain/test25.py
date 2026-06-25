from langchain_community.document_loaders import PyPDFLoader, UnstructuredMarkdownLoader
from langchain_core.documents import Document

# 手动定义的文档列表
documens = [

    # 对于单个的Document文档，它一般表示较大的文档的某一块或某一页
    Document(
        # 内容
        page_content="狗是忠实的伴侣",
        # 元数据字典
        # 元数据属性可以包含：文档源,与其他文档的关系以及其他属性信息
        metadata={"source":"pets_doc"},
    ),
    Document(
        # 内容
        page_content="猫是独立的宠物",
        # 元数据字典
        # 元数据属性可以包含：文档源,与其他文档的关系以及其他属性信息
        metadata={"source":"pets_doc"},
    )
]

# 文档加载器(PDF)
loader = PyPDFLoader(file_path="../Docs/pdf/自然资源主题新媒体科普宣传的实践与探索.pdf")
# 加载：生成文档列表
docs = loader.load()

# PDF加载器默认将文档按分页进行拆分
print(f"PDF文档总页数：{len(docs)}\n")
print(f"第一页文本的内容（前200）是：\n{docs[0].page_content[:200]}\n")
print(f"第一页的元数据字典是:\n{docs[0].metadata}\n")

# 文档加载器
md_loader = UnstructuredMarkdownLoader(
    "../Docs/markdown/自然资源主题新媒体科普宣传的实践与探索.md",
    # mode = "single"  # MD 加载器默认将文档加载为一个
    mode = "elements"
)
# Document 列表
docs = md_loader.load()

print(f"MD文档总页数：{len(docs)}\n")
print(f"第一页文档的内容是：\n{docs[0].page_content}\n")

print(f"当前MD文档的所有分类：{set(document.metadata["category"] for document in docs )}\n")