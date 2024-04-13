import os
from typing import Union
from fastapi import Request,FastAPI
# from models import postbackModel 
import httpx
from dotenv import load_dotenv
import json

load_dotenv()

app = FastAPI()

async def send_telegram_message(message):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        if response.status_code == 200:
            print("Message sent successfully!")
        else:
            print("Failed to send message. Error:", response.text)

@app.post("/postback")
async def postback_handler(request: Request):
    # await print(request.body())
    postbackData = await request.json()
    await send_telegram_message("Postback received!\n" + json.dumps(postbackData))
    return postbackData

