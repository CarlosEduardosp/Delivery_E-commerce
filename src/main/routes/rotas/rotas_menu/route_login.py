from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_login = Blueprint("rota_login", __name__)


@api_routes_bp_login.route(
    "/efetuar_login/<apelido>/<quantidade_carrinho>", methods=["GET", "POST"]
)
def login(apelido: str, quantidade_carrinho: int):
    """Realiza o login comparando os dados inseridos, com os da tabela Cliente."""

    # instancia clientes, HttpRequest e selct de todos os clientes.
    clientes = AdapterCliente(api_route=register_cliente_composer(), data={})
    clientes = clientes.select_all()

    # request do email e senhao do form
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        # comparando senha digitada com senha salva no banco
        for cliente in clientes.body:
            if cliente.email == email and senha == cliente.senha:
                # coletando quantidade de produtos no carrinho de clientes
                quantidade_carrinho = AdapterCarrinho(
                    api_route=register_carrinho_composer(),
                    data={"id_cliente": cliente.id_cliente},
                )
                quantidade_carrinho = quantidade_carrinho.select()
                # selecionando a quantidade de itens no carrinho dentro do "Len"
                quantidade_carrinho = quantidade_carrinho.body["Len"]

                apelido = cliente.apelido

                return redirect(
                    url_for(
                        "home.home",
                        apelido=apelido,
                        quantidade_carrinho=quantidade_carrinho,
                    )
                )

        # exibi mensagem de erro caso senha ou email sejam inválidos.
        mensagem = "Usuário não encontrado ou senha incorreta!!"
        flash(mensagem)

    return render_template(
        "login.html", apelido=apelido, quantidade_carrinho=quantidade_carrinho
    )
