from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://english-learning-assistant-omega.vercel.app","https://www.google.com"],  # 你的前端網址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat(msg: Message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "你是一位英文家教，幫助 TOEIC 300 初學者學英文。請用簡單英文對話，幫忙糾正錯誤並提供說明。"
            },
            {
                "role": "user",
                "content": msg.message
            }
        ]
    )
    return {"reply": response.choices[0].message.content}
