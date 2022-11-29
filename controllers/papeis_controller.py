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

# Endpoint to create the item
@router.post("/")
async def add_item(papel: Papel):
    await papel.save()
    return papel

# Endpoint to get all the objects added on database
@router.get("/")
async def list_item():
    return await Papel.objects.all()