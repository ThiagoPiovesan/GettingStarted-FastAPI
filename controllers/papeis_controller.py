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
from fastapi import APIRouter

from models.papel import Papel

router = APIRouter()

# fake database
banco_de_dados = []

# Endpoint to create the item
@router.post("/")
def add_item(item: Papel):
    banco_de_dados.append(item)
    return item

# Endpoint to get all the objects added on database
@router.get("/")
def list_item():
    return banco_de_dados
