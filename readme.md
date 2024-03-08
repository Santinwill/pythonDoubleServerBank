```
Instalacoes necessarias

pip install fastapi
pip install uvicorn[standard]
pip install requests
pip install pytest
pip install httpx

```
```
Subir o servidor endpoints
python -m uvicorn endpoints:app --port 8000 --reload

subir o servidor manager
python -m uvicorn manager:app --port 8001 --reload

```
```
documentacao Swagger

http://127.0.0.1:8000/docs
http://127.0.0.1:8001/docs

```
```
Rodar os testes
python -m pytest test.py

```
```
docker

subir docker
docker-compose up --build 

buildar imagem        CAMINHO DOCKERFILE                 NOME
docker build -f .\Dockerfiles\endpoints\Dockerfile . -t imagemwill

encontrando o ID do conteiner
docker container ls

ajustar tag
docker tag imagemwill:latest santinwill1995/imagemwill:latest

subir imagem
docker push santinwill1995/imagemwill:latest

http://127.0.0.1:8001/docs

http://127.0.0.1:8001/clientes/2
```