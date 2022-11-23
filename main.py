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

# Criação do app
app = FastAPI()

# definição das rotas
@app.get("/")                                       # Método GET
def read_root():
    return {"Hello": "World 2"}

# definição das rotas
@app.get("/items/{item_id}")                        # Método GET
def read_item(item_id: int, p: bool, q: Union[str, None] = None):
    return {"item_id": item_id, "p": p, "q": q}