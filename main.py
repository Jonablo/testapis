from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Optional
from test_ia.openiatest import Document, inference
from test_ia.contvocal import Document, conta
from test_ia.conBi import Document, conBi

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)

class libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str]


@app.get("/")
def index():
    return {"message": "hola, fastapi"}


@app.get("/libros/{id}")
def mostrar_libros(id: int):
    return {"data": id}


@app.post("/libros")
def insertar_libro(libro: libro):
    return {"message": f"el libro {libro.titulo} ha sido instertado"}


@app.post("/inference", status_code=200)
def inference_endpoint(doc: Document):
    response = inference(doc.prompt)
    return {"inference": response[0], "tokens usados": response[1]}


@app.post("/conta", status_code=200)
def conta_endpoint(doc: Document):
    response = conta(doc.prompt)
    return {"respuesta": response[0], "tokens usados": response[1]}


@app.post("/conBi", status_code=200)
def conBi_endpoint(doc: Document):
    response = conBi(doc.prompt)
    return {"respuesta": response[0], "tokens usados": response[1]}