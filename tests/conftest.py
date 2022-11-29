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
import os
import pytest

from fastapi.testclient import TestClient
from typing import Generator

from main import app
from cria_tabelas import configurar_banco

# Enviroment variables:
DATABASE_URL = 'sqlite:///testedb.sqlite'
os.environ["DATABASE_URL"] = DATABASE_URL
os.environ["TEST_DATABASE"] = 'true'
#==================================================================================================#
# Test Init
@pytest.fixture(scope="function")
def client() -> Generator:
    configurar_banco(DATABASE_URL)
    with TestClient(app) as c:
        yield c         # return all possibilities
        
