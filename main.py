from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Criação de modelo Pydantic para o corpo da requisição
class UserRequest(BaseModel):
    user: str

@app.post("/auth/me")
async def auth_me(user_request: UserRequest):
    user = user_request.user  # Pega o valor do campo "user"
    return {"user": user, "ping": "pong"}
