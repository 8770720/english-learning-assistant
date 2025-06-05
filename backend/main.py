from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
from fastapi.middleware.cors import CORSMiddleware

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
openai.api_key = os.getenv("OPENAI_API_KEY")

# 接收前端傳來的資料格式
class Message(BaseModel):
    message: str

# 路由：接收 POST 到 /chat 的請求
@app.post("/chat")
async def chat(msg: Message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 若要用 GPT-4，請改為 "gpt-4"
        messages=[
            {
                "role": "system",
                "content": (
                    "你是一位英文家教，幫助 TOEIC 300 初學者學習英文。"
                    "請用簡單英文進行對話，當學生輸入錯誤時，請給出修正版本，並簡單解釋為什麼。"
                    "請使用鼓勵的語氣，不要使用太難的單字。"
                )
            },
            {
                "role": "user",
                "content": msg.message
            }
        ]
    )
    return {"reply": response["choices"][0]["message"]["content"]}
