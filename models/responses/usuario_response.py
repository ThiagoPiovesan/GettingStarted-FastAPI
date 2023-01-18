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
from pydantic import BaseModel
from typing import List

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    funcoes: List[str]