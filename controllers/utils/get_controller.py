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
from functools import wraps

from controllers.utils.entidade_nao_encontrada import entidade_nao_encontrada

def get_controller(modelo: ormar.Model, select_related=[]):
    def inner(func):
        @entidade_nao_encontrada
        @wraps(func)
        async def wrapper(id: int, **kwargs):
            
            consulta = modelo.objects
            if len(select_related):
                consulta = consulta.select_related(select_related)
                
            entidade = await modelo.objects.get(id=id)
            return entidade
        return wrapper
    return inner