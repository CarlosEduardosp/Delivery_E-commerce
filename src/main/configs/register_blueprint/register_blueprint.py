from .imports_blueprint import *  # noqa


class RegisterBlueprint:
    """registrar bluePrint"""

    __lista_rotas = [
        api_routes_bp_home,
        api_routes_bp_login,
        api_routes_bp_cad_cliente,
        api_routes_bp_validar,
        api_routes_bp_produto,
        api_routes_bp_cad_produto,
        api_routes_bp_carrinho,
        api_routes_bp_adicionar_carrinho,
        api_routes_bp_clientes,
        api_routes_bp_pedidos_cliente,
        api_routes_bp_del_cliente,
        api_routes_bp_del_produto,
        api_routes_bp_del_carrinho,
        api_routes_bp_editar_produto,
        api_routes_bp_perfil,
        api_routes_bp_pedido,
        api_routes_bp_confirmar_pedido,
        api_routes_bp_sair,
        api_routes_bp_controle_pedido,
        api_routes_bp_atualizar_status_pedido,
    ]

    def __init__(self, app: None):
        self.app = app
        self.__registrar_blueprint()

    def __registrar_blueprint(self):
        """registrando as rotas no app"""

        for bp in self.__lista_rotas:
            self.app.register_blueprint(bp)

        return self.app
