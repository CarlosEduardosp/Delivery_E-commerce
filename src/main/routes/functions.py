from src.main.composer.register_codigo_composer import register_codigo_composer
from src.presenters.helpers.http_models import HttpRequest


def validador_senha(senha: any, confirmar_senha: any) -> bool:
    """verifica se as senhas são iguais"""

    if senha:
        if senha == confirmar_senha:
            return True
    else:
        return False


def comparar_codigo(codigo: int):
    """realiza a comparação de codigo"""
    http_request = HttpRequest(query={"id_cliente": 1})
    comparar = register_codigo_composer()

    if codigo:
        codigo = int(codigo)
        response = comparar.route_select(http_request)

        for i in response.body:
            print(i.codigo)
            if codigo == i.codigo:
                return True

        return False
