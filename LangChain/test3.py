from langchain.chat_models import init_chat_model
from openai import base_url

ollma_model = init_chat_model(modell="deepseek-r1:1.5b",base_url = "http://127.0.0.1:11434")
print(ollma_model.invoke("你是谁").content)