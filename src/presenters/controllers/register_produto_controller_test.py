from faker import Faker
from src.data.registrar_produto.register_produto import RegisterProduto
from src.infra.repo.produto_Repository import ProdutoRepository
from src.presenters.helpers.http_models import HttpRequest
from .register_produto_controller import RegisterProdutoController


faker = Faker()


def test_handle():
    """Testing Handle method"""

    register_produto_use_case = RegisterProduto(ProdutoRepository())
    register_produto_controller = RegisterProdutoController(register_produto_use_case)

    http_request = HttpRequest(
        query={
            "nome": faker.name(),
            "descricao": faker.email(),
            "imagem": faker.name(),
            "preco": float(faker.random_number(digits=2)),
        }
    )

    response = register_produto_controller.handle_insert(http_request)

    return response


def test_select_controller():
    """testing controller select"""

    register_produto_use_case = RegisterProduto(ProdutoRepository())
    register_produto_controller = RegisterProdutoController(register_produto_use_case)

    http_request = HttpRequest(query={"id_produto": faker.random_number(digits=1)})

    response = register_produto_controller.handle_select(http_request)

    return response


def test_select_all_controller():
    """testing select all"""

    register_produto_use_case = RegisterProduto(ProdutoRepository())
    register_produto_controller = RegisterProdutoController(register_produto_use_case)

    http_request = HttpRequest()
    response = register_produto_controller.handle_select_all(http_request)

    return response


def test_delete_controller():
    """testing controller delete"""

    register_produto_use_case = RegisterProduto(ProdutoRepository())
    register_produto_controller = RegisterProdutoController(register_produto_use_case)

    http_request = HttpRequest(query={"id_produto": faker.random_number(digits=2)})

    response = register_produto_controller.handle_delete(http_request)

    return response


def test_handle_update():
    """Testing Handle method"""

    register_produto_use_case = RegisterProduto(ProdutoRepository())
    register_produto_controller = RegisterProdutoController(register_produto_use_case)

    http_request = HttpRequest(
        query={
            "id_produto": 3,
            "nome": faker.name(),
            "descricao": faker.email(),
            "imagem": faker.name(),
            "preco": float(faker.random_number(digits=2)),
        }
    )

    response = register_produto_controller.handle_update(http_request)

    return response
