from src.main.composer.register_codigo_composer import register_codigo_composer
from src.main.adapter.adapter_codigo.adapter_codigo import AdapterCodigo


def validador_senha(senha: any, confirmar_senha: any) -> bool:
    """verifica se as senhas são iguais"""

    if senha:
        if senha == confirmar_senha:
            return True
    else:
        return False


def comparar_codigo(codigo: int) -> bool:
    """realiza a comparação de codigo"""
    codigobd = AdapterCodigo(
        api_route=register_codigo_composer(), data={"id_cliente": 1}
    )
    response = codigobd.select()

    if response.status_code == 200:
        codigo = int(codigo)
        if response.body.codigo == codigo:
            return True
        return False
