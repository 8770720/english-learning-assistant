from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
from fastapi.middleware.cors 
import CORSMiddleware from openai import OpenAI

client = OpenAI()

app = FastAPI()

# 允許跨來源請求（讓前端能呼叫後端 API）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 如有需要可改為前端網址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 從環境變數讀取 OpenAI API 金鑰
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 接收前端傳來的資料格式
class Message(BaseModel):
    message: str

# 路由：接收 POST 到 /chat 的請求
@app.post("/chat")
async def chat(msg: Message):
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "你是一位英文家教，幫助 TOEIC 初學者..."},
        {"role": "user", "content": msg.message}
      ]
    )
    return {"reply": response["choices"][0]["message"]["content"]}
