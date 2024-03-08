from fastapi import FastAPI, HTTPException, Body
from model import Transacao, AtualizarTransacao
import requests



app = FastAPI()

@app.post("/clientes/{id_cliente}/transacoes")
async def criar_transacao_manager(id_cliente: int, transacao: Transacao):
    url = f"http://127.0.0.1:8000/api/clientes/{id_cliente}/transacoes"
    response = requests.post(url, json=transacao.dict())
    return response.json()

@app.get("/clientes/{id_cliente}/transacoes")
async def listar_transacoes_manager(id_cliente: int):
    url = f"http://127.0.0.1:8000/api/clientes/{id_cliente}/transacoes"
    response = requests.get(url)
    return response.json()

@app.get("/clientes/{id_cliente}/transacoes/{transacao_id}")
async def obter_transacao_manager(id_cliente: int, transacao_id: int):
    url = f"http://127.0.0.1:8000/api/clientes/{id_cliente}/transacoes/{transacao_id}"
    response = requests.get(url)
    return response.json()

@app.put("/clientes/{id_cliente}/transacoes/{transacao_id}")
async def atualizar_transacao_manager(id_cliente: int, transacao_id: int, transacao_atualizada: AtualizarTransacao):
    url = f"http://127.0.0.1:8000/api/clientes/{id_cliente}/transacoes/{transacao_id}"
    response = requests.put(url, json=transacao_atualizada.dict())
    return response.json()

@app.delete("/clientes/{id_cliente}/transacoes/{transacao_id}")
async def deletar_transacao_manager(id_cliente: int, transacao_id: int):
    url = f"http://127.0.0.1:8000/api/clientes/{id_cliente}/transacoes/{transacao_id}"
    response = requests.delete(url)
    return response.json()

@app.get("/clientes/{id_cliente}")
async def obter_cliente_manager(id_cliente: int):
    url = f"http://127.0.0.1:8000/api/clientes/{id_cliente}"
    response = requests.get(url)
    return response.json()