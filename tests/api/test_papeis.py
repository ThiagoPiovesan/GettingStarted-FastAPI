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
import asyncio
from fastapi.testclient import TestClient
from models.papel import Papel
from tests.utils.papeis import create_papel_valido, create_papel_invalido

#-----------------------------------------------------------------------------
def test_cria_papel(client: TestClient) -> None:
    body = create_papel_valido()
    response = client.post("/papeis/", json=body)
    content = response.json()
    
    assert response.status_code == 200
    assert content["cnpj"] == body["cnpj"]
    
def test_cria_papel_com_sigla_invalida(client: TestClient) -> None:
    body = create_papel_invalido(['sigla'])
    response = client.post("/papeis/", json=body)
    content = response.json()
    
    assert response.status_code == 422
    
#-----------------------------------------------------------------------------
# Test GET
def test_obtem_um_papel_por_id(client: TestClient) -> None:
    atributos = create_papel_valido()
    papel = Papel(**atributos)

    # The old way: loop = asyncio.get_event_loop()
    # The new way:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    #------
    loop.run_until_complete(papel.save())
    
    response = client.get(f"/papeis/{papel.id}")
    content = response.json()
    
    assert response.status_code == 200
    assert content["sigla"] == papel.sigla
    
def test_obtem_um_papel_inexistente_por_id(client: TestClient) -> None: 
    response = client.get(f"/papeis/1")
    content = response.json() 
    
    assert response.status_code == 404
    assert content["mensagem"] == "Entidade não encontrada!"
    
#-----------------------------------------------------------------------------
# Test Update
def test_update_papel_existente(client: TestClient) -> None:
    atributos = create_papel_valido()
    papel = Papel(**atributos)
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    #------
    loop.run_until_complete(papel.save())
    
    novo_nome = "Novo nome"
    atributos_para_atualizar = {"nome": novo_nome}
    
    response = client.patch(f"/papeis/{papel.id}", json=atributos_para_atualizar)
    content = response.json()
    
    papel_atualizado = loop.run_until_complete(Papel.objects.get(id=papel.id))
    
    assert response.status_code == 200
    assert content["nome"] == novo_nome
    assert papel_atualizado.nome == novo_nome
    
def test_update_papel_inexistente(client: TestClient) -> None:
    novo_nome = "Novo nome"
    atributos_para_atualizar = {"nome": novo_nome}
    
    response = client.patch(f"/papeis/1", json=atributos_para_atualizar)
    content = response.json()
    
    assert response.status_code == 404
    assert content["mensagem"] == "Entidade não encontrada!"
    
#-----------------------------------------------------------------------------
