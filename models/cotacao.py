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
import datetime
from typing import Optional

from config import database, metadata
from models.papel import Papel

class Cotacao(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "cotacoes"
        
    id: int = ormar.Integer(primary_key=True)
    valor: float = ormar.Float(minimum=0)
    horario: datetime = ormar.DateTime(timezone=False)
    
    papel: Optional[Papel] = ormar.ForeignKey(
        Papel,
        skip_reverse = True # Não deixa criar automaticamente uma propriedade dentre de Papeis
    )