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
from fastapi.testclient import TestClient

def test_get_root(client: TestClient) -> None:
    response = client.get('/')
    body = response.json()
    
    assert response.status_code == 200
    assert body["mensagem"] == "API de Papeis"