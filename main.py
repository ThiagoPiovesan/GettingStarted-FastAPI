# /*==========================================================*\
# |      /=============================================\       |
# |     ||  -    FastAPI Framework implementation    - ||      |
# |     ||  -       Adapted by: Thiago Piovesan      - ||      |
# |     ||  -          Versao atual: 1.0.0           - ||      |
# |      \=============================================/       |
# \*==========================================================*/

# Link do Github: https://github.com/ThiagoPiovesan

#==================================================================================================#
# Bibliotecas utilizadas:
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    quantidade: int
    descricao: str
    valor: float

# Criação do app
app = FastAPI()

# fake database
banco_de_dados = []

# Endpoint to create the item
@app.post("/item")
def add_item(item: Item):
    banco_de_dados.append(item)
    return item

# Endpoint to get all the objects added on database
@app.get("/item")
def list_item():
    return banco_de_dados

@app.get("/item/valor_total")
def get_valor_total():
    valor_total:float = sum(item.valor * item.quantidade for item in banco_de_dados)
    
    return {"Valor_total: ": valor_total}