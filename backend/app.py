from fastapi import FastAPI, Request
from pydantic import BaseModel
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

class UserMessage(BaseModel):
    message: str

@app.post("/chat")
def chat(user_msg: UserMessage):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "你是一位英文家教，幫助 TOEIC 300 學生學英文..."},
            {"role": "user", "content": user_msg.message}
        ]
    )
    return {"reply": response["choices"][0]["message"]["content"]}
