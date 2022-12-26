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
import pydantic
import ormar
from fastapi import APIRouter

from models.papel import Papel
from models.requests.papel_update import PapelUpdate
from controllers.utils.entidade_nao_encontrada import entidade_nao_encontrada

from controllers.utils.delete_controller import delete_controller
from controllers.utils.patch_controller import patch_controller
from controllers.utils.get_controller import get_controller
from controllers.utils.get_all_controller import get_all_controller
from controllers.utils.post_controller import post_controller

router = APIRouter()

# Endpoint to create the item
@router.post("/")
@post_controller
async def add_item(entidade: Papel):
    pass

# Endpoint to get all the objects added on database
@router.get("/")
@get_all_controller(Papel)
async def list_item():
    pass

@router.get("/{id}")
@get_controller(Papel)
async def get_papel(id: int):
    pass

#Endpoint to update infos
@router.patch("/{id}")
@patch_controller(Papel)
async def patch_papel(propriedades_atualizacao: PapelUpdate, id: int):
    pass
    
#Endpoint to delete infos
@router.delete("/{id}")
@delete_controller(Papel)
async def delete_papel(id: int):
    pass
