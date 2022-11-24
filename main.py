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
from fastapi import FastAPI, Header, Response, Cookie
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    descricao: str
    valor: float

# Criação do app
app = FastAPI()

# definição das rotas
@app.get("/")                                       # Método GET
def read_root(user_agent: Union[str, None] = Header(None)):
    return {"user_agent": user_agent}

# definição das rotas
@app.get("/cookie")                                 # Método GET
def cookie(response: Response):
# Informações gravadas do lado do cliente, gravar alguma sessão
# ou preferência do usuário.
    response.set_cookie(key="meucookie", value="123-456")
    return {"cookie": True}

# definição das rotas
@app.get("/get-cookie")                             # Método GET
def get_cookie(meucookie: Union[str, None] = Cookie(None)):
    return {"Cookie": meucookie}

# definição das rotas
@app.get("/items/{item_id}")                        # Método GET
def read_item(item_id: int, p: bool, q: Union[str, None] = None):
    return {"item_id": item_id, "p": p, "q": q}

# definição das rotas
@app.post("/item")                                  # Método POST       
def add_item(novo_item: Item):
    return novo_item
    