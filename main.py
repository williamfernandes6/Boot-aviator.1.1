from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from auth import verify_user
from utils import gerar_sinal
import json

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sinal")
async def get_sinal(casa: str = "ElephantBet"):
    sinal = gerar_sinal(casa)
    return {"casa": casa, "sinal": sinal}

@app.post("/login")
async def login(request: Request):
    body = await request.json()
    username = body.get("username")
    password = body.get("password")
    if verify_user(username, password):
        return {"status": "success", "vip": True}
    raise HTTPException(status_code=401, detail="Credenciais inválidas")