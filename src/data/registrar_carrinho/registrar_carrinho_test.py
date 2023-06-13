from faker import Faker
from .registrar_carrinho import RegisterCarrinho
from src.infra.repo.carrinho_Repository import CarrinhoRepository

faker = Faker()


def test_register_carrinho():
    """testing registry method"""

    user_repo = CarrinhoRepository()
    register_car = RegisterCarrinho(user_repo)

    response = None

    try:
        response = register_car.insert_carrinho(
            id_produto=faker.random_number(digits=1),
            id_cliente=faker.random_number(digits=1),
        )
        return response
    except:
        return {"Success": False, "Data": response}

    return None


def test_select_carrinho():
    """testing select carrinho"""

    user_repo = CarrinhoRepository()
    register_car = RegisterCarrinho(user_repo)

    response = None

    try:
        response = register_car.select_carrinho(id_cliente=2)
        return response
    except:
        return response


def test_delete_carrinho():
    """testing delete carrinho"""

    user_repo = CarrinhoRepository()
    register_car = RegisterCarrinho(user_repo)

    response = None
    try:
        response = register_car.delete_carrinho(id_cliente=5, id_produto=4)
        return response
    except:
        return response


def test_select_all_carrinho():
    """testing select all"""

    user_repo = CarrinhoRepository()
    register_car = RegisterCarrinho(user_repo)

    try:
        response = register_car.select_all_carrinho()
        return response
    except:
        return None
