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
from src.main.composer.register_pedido_composer import register_pedido_composer
from src.doman.models.cliente import Cliente
from src.main.adapter.adapter_cliente.adapter_cliente import AdapterCliente
from src.main.adapter.adapter_buscar_cep.flask_adapter_buscar_cep import BuscarCep
from src.main.adapter.adapter_produto.adapter_produto import AdapterProduto
from src.main.adapter.adapter_carrinho.adapter_carrinho import AdapterCarrinho
from src.main.adapter.adapter_codigo.adapter_codigo import AdapterCodigo
from src.main.adapter.adapter_endereco.adapter_endereco import AdapterEndereco
from src.main.adapter.adapter_pedido.adapter_pedido import AdapterPedido
from faker import Faker
import os
import requests
from datetime import date, datetime

# import json

pass
