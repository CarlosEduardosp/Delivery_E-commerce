# flake8: noqa
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
    json,
)
from src.main.composer.register_produto_composer import register_produto_composer
from src.main.composer.buscar_cep_composer import buscar_cep_composer
from src.presenters.helpers.http_models import HttpRequest
from .functions import validador_senha, comparar_codigo
from src.data.enviar_codigo_email.enviar_codigo import EnviarCodigoEmail
from src.main.composer.register_codigo_composer import register_codigo_composer
from src.main.composer.register_cliente_composite import register_cliente_composer
from src.main.composer.register_carrinho_composer import register_carrinho_composer
from src.main.composer.register_endereco_composer import register_endereco_composer
from src.doman.models.cliente import Cliente
from src.main.adapter.adapter_cliente.flask_adapter_cliente import flask_adapter_cliente
from src.main.adapter.adapter_buscar_cep.flask_adapter_buscar_cep import (
    flask_adapter_buscar_cep,
)
from src.main.adapter.adapter_produto.flask_adapter_produto import flask_adapter_produto
from src.main.adapter.adapter_carrinho.flask_adapter_carrinho import (
    flask_adapter_carrinho,
)
from src.main.adapter.adapter_codigo.flask_adapter_codigo import flask_adapter_codigo
from src.main.adapter.adapter_endereco.flask_adapter_endereco import (
    flask_adapter_endereco,
)
from faker import Faker
import os
import requests

# import json

pass
