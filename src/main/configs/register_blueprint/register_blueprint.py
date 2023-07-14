from .imports_blueprint import *  # noqa


class RegisterBlueprint:
    """registrar bluePrint"""

    def __init__(self, app: None):
        self.app = app
        self.__registrar_blueprint()

    def __registrar_blueprint(self):
        """registrando as rotas no app"""

        self.app.register_blueprint(api_routes_bp_home)
        self.app.register_blueprint(api_routes_bp_login)
        self.app.register_blueprint(api_routes_bp_cad_cliente)
        self.app.register_blueprint(api_routes_bp_validar)
        self.app.register_blueprint(api_routes_bp_produto)
        self.app.register_blueprint(api_routes_bp_cad_produto)
        self.app.register_blueprint(api_routes_bp_carrinho)
        self.app.register_blueprint(api_routes_bp_adicionar_carrinho)
        self.app.register_blueprint(api_routes_bp_clientes)
        self.app.register_blueprint(api_routes_bp_pedidos_cliente)
        self.app.register_blueprint(api_routes_bp_del_cliente)
        self.app.register_blueprint(api_routes_bp_del_produto)
        self.app.register_blueprint(api_routes_bp_del_carrinho)
        self.app.register_blueprint(api_routes_bp_editar_produto)
        self.app.register_blueprint(api_routes_bp_perfil)
        self.app.register_blueprint(api_routes_bp_pedido)
        self.app.register_blueprint(api_routes_bp_confirmar_pedido)
        self.app.register_blueprint(api_routes_bp_sair)
        self.app.register_blueprint(api_routes_bp_controle_pedido)

        return self.app
