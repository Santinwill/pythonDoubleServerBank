from fastapi import FastAPI, HTTPException
from model import Cliente, Transacao, AtualizarTransacao
from services import (criar_transacao_service, listar_transacoes_service, obter_transacao_service, 
                      atualizar_transacao_service, deletar_transacao_service, obter_cliente_service)
from typing import List

app = FastAPI()

@app.post("/api/clientes/{id_cliente}/transacoes")
async def criar_transacao_endpoint(id_cliente: int, transacao: Transacao):
    return criar_transacao_service(id_cliente, transacao)

@app.get("/api/clientes/{id_cliente}/transacoes", response_model=List[Transacao])
async def listar_transacoes_endpoint(id_cliente: int):
    return listar_transacoes_service(id_cliente)
    
@app.get("/api/clientes/{id_cliente}/transacoes/{transacao_id}", response_model=Transacao)
async def obter_transacao_endpoint(id_cliente: int, transacao_id: int):
    return obter_transacao_service(id_cliente, transacao_id)

@app.put("/api/clientes/{id_cliente}/transacoes/{transacao_id}", response_model=Transacao)
async def atualizar_transacao_endpoint(id_cliente: int, transacao_id: int, transacao_atualizada: AtualizarTransacao):
    return atualizar_transacao_service(id_cliente, transacao_id, transacao_atualizada)
            
@app.delete("/api/clientes/{id_cliente}/transacoes/{transacao_id}")
async def deletar_transacao_endpoint(id_cliente: int, transacao_id: int):
    return deletar_transacao_service(id_cliente, transacao_id)

@app.get("/api/clientes/{id_cliente}", response_model=Cliente)
async def obter_cliente_endpoint(id_cliente: int):
    return obter_cliente_service(id_cliente)