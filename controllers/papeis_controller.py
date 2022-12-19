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
from fastapi import APIRouter, Response

from models.papel import Papel
from models.requests.papel_update import PapelUpdate

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
    
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return {"mensagem": "Entidade não encontrada!"}
    
#Endpoint to update infos
@router.patch("/{papel_id}")
async def patch_papel(propriedades_atualizacao: PapelUpdate, papel_id: int, response: Response):
    try:
        papel_salvo = await Papel.objects.get(id=papel_id)
        propriedades_atualizadas = propriedades_atualizacao.dict(exclude_unset=True)
        await papel_salvo.update(**propriedades_atualizadas)
        return papel_salvo
    
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return {"mensagem": "Entidade não encontrada!"}
    
#Endpoint to delete infos
@router.delete("/{papel_id}")
async def delete_papel(papel_id: int, response: Response):
    try:
        papel = await Papel.objects.get(id=papel_id)
        return await papel.delete()
    
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return {"mensagem": "Entidade não encontrada!"}