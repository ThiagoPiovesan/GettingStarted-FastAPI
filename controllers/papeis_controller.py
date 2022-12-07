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
from fastapi import APIRouter, Response

from models.papel import Papel

router = APIRouter()

# Endpoint to create the item
@router.post("/")
async def add_item(papel: Papel):
    await papel.save()
    return papel

# Endpoint to get all the objects added on database
@router.get("/")
async def list_item():
    return await Papel.objects.all()

@router.get("/{papel_id}")
async def get_papel(papel_id: int, response: Response):
    
    try:
        papel = await Papel.objects.get(id=papel_id)
        return papel
    
    except pydantic.error_wrappers.ValidationError:
        response.status_code = 404
        return {"mensagem": "Entidade não encontrada!"}