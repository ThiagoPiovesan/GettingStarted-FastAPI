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
import ormar
from fastapi import HTTPException
from functools import wraps

def entidade_nao_encontrada(func):
    @wraps(func)
    async def inner(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        
        except ormar.exceptions.NoMatch:
            raise HTTPException(status_code=404, detail="Entidade não encontrada!")
        
    return inner