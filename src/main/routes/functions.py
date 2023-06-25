from src.main.composer.register_codigo_composer import register_codigo_composer
from src.presenters.helpers.http_models import HttpRequest
import random


def validador_senha(senha: any, confirmar_senha: any) -> bool:
    """verifica se as senhas são iguais"""

    if senha == confirmar_senha:
        return True
    else:
        return False


def criar_codigo_confirmacao():
    """monta o codigo de confirmação que será enviado por email"""

    codigo1 = random.randint(0, 9)
    codigo2 = random.randint(0, 9)
    codigo3 = random.randint(0, 9)
    codigo4 = random.randint(0, 9)
    codigo = str(codigo1) + str(codigo2) + str(codigo3) + str(codigo4)
    codigo = int(codigo)

    # salvando o codigo no banco de dados
    registrar_codigo = register_codigo_composer()
    http_request = HttpRequest(query={"codigo": codigo, "id_cliente": 1})

    response = registrar_codigo.route_insert(http_request)

    return response


def comparar_codigo(codigo: int):
    """realiza a comparação de codigo"""
    http_request = HttpRequest(query={"id_cliente": 1})
    comparar = register_codigo_composer()

    if codigo:
        codigo = int(codigo)
        response = comparar.route_select(http_request)
        for i in response.body:
            if codigo == i.codigo:
                return True
            else:
                return False
