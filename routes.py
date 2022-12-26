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

from controllers import papeis_controller as papeis
from controllers import cotacoes_controller as cotacoes

router = APIRouter()

router.include_router(papeis.router, prefix='/papeis', tags=['Papeis'])

router.include_router(cotacoes.router, prefix='/cotacoes', tags=['Cotacoes'])