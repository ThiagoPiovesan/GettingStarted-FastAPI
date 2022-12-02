# /*==========================================================*\
# |      /=============================================\       |
# |     ||  -    FastAPI Framework implementation    - ||      |
# |     ||  -      Adapted by: Thiago Piovesan       - ||      |
# |     ||  -         Versao atual: 1.0.0            - ||      |
# |      \=============================================/       |
# \*==========================================================*/

# Link do Github: https://github.com/ThiagoPiovesan

#==================================================================================================#

def create_papel_valido():
    return {
        "id": 0,
        "nome": "string",
        "sigla": "PETR4",
        "cnpj": "string",
    }
    
def create_papel_invalido(campos_invalidos=['sigla']):
    papel_invalido = {
        "id": 0,
        "nome": "string",
        "sigla": "PETR4",
        "cnpj": "string", 
    }
    
    if 'sigla' in campos_invalidos:
        papel_invalido['sigla'] = "AAAAAAA"
        
    return papel_invalido