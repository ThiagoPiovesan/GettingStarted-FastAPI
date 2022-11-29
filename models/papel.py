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
from config import database, metadata

# Class Definition:
class Papel(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "papeis"
    
    id: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(max_length=100)
    sigla: str = ormar.String(max_length=10)
    cnpj: str = ormar.String(max_length=20)
