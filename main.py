# FastAPI
from fastapi import FastAPI, Header, HTTPException, Depends, status, Response, Request
from fastapi.responses import JSONResponse, HTMLResponse
import uvicorn

# Line-Bot SDK
from linebot import *

# Router
from routers.line_bot import bot
from routers.user import user

# Initiate Fast App
app = FastAPI()

# Router to Fast App
app.include_router(bot.router)
app.include_router(user.router)

@app.get('/')
async def root():
    return {'message': 'Hellooooo'}

@app.get("/liff", response_class=HTMLResponse)
async def read_item(request: Request):
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)