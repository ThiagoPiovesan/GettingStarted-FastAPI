# /*==========================================================*\
# |      /=============================================\       |
# |     ||  -    FastAPI Framework implementation    - ||      |
# |     ||  -      Adapted by: Thiago Piovesan       - ||      |
# |     ||  -         Versao atual: 1.0.0            - ||      |
# |      \=============================================/       |
# \*==========================================================*/

# Link do Github: https://github.com/ThiagoPiovesan

#==================================================================================================#
# Bibliotecas utilizadas:
from fastapi import FastAPI

from routes import router

# Criação do app
app = FastAPI()

@app.get("/")
def get_root():
    return {"mensagem": "API de Papeis"}

app.include_router(router, prefix="")