from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_perfil = Blueprint("rota_perfil", __name__)


@api_routes_bp_perfil.route(
    "/perfil/<apelido>/<quantidade_carrinho>", methods=["GET", "POST"]
)
def perfil(apelido: str, quantidade_carrinho: int):
    """Perfil com os dados do cliente ou administrador"""

    # seleciona todos os clientes e endereços
    cliente = AdapterCliente(api_route=register_cliente_composer(), data={})
    clientes = cliente.select_all()
    endereco = AdapterEndereco(api_route=register_endereco_composer(), data={})
    endereco_cliente = endereco.select_all()

    # faz o request dos dados passados via formulário
    if request.method == "POST":
        email = request.form.get("email")
        apelido_request = request.form.get("apelido")
        cep_cliente = request.form.get("cep_cliente")
        estado = request.form.get("estado")
        cidade = request.form.get("cidade")
        bairro = request.form.get("bairro")
        logradouro = request.form.get("logradouro")
        complemento = request.form.get("complemento")

        # verifica se todos os campos foram preenchidos
        if (
            email
            and apelido_request
            and cep_cliente
            and estado
            and cidade
            and bairro
            and logradouro
            and complemento
        ):
            # compara o cliente com a lista de clientes e em seguida realiza o update
            for i in clientes.body:
                if apelido == i.apelido:
                    cliente = AdapterCliente(
                        api_route=register_cliente_composer(),
                        data={
                            "id_cliente": i.id_cliente,
                            "apelido": apelido_request,
                            "email": email,
                            "senha": i.senha,
                            "cep_cliente": cep_cliente,
                        },
                    )
                    cliente.update()

                #  realiza o update do endereço do cliente selecionado
                for x in endereco_cliente.body:
                    if i.id_cliente == x.id_cliente:
                        endereco = AdapterEndereco(
                            api_route=register_endereco_composer(),
                            data={
                                "id_endereco": x.id_endereco,
                                "cep_cliente": cep_cliente,
                                "estado": estado,
                                "cidade": cidade,
                                "bairro": bairro,
                                "logradouro": logradouro,
                                "complemento": complemento,
                                "id_cliente": i.id_cliente,
                            },
                        )
                        endereco.update()

            # envia uma msg de confirmação do update
            mensagem = f"{apelido}, Seus Dados Foram Alterados com Sucesso."
            flash(mensagem)
            return redirect(
                url_for(
                    "rota_perfil.perfil",
                    apelido=apelido_request,
                    quantidade_carrinho=quantidade_carrinho,
                )
            )
    # salva o conteudo dentro do Body para enviar ao template perfil.html
    clientes = cliente.select_all()
    clientes = clientes.body
    endereco = endereco.select_all()
    endereco = endereco.body

    return render_template(
        "perfil.html",
        apelido=apelido,
        quantidade_carrinho=quantidade_carrinho,
        clientes=clientes,
        endereco=endereco,
    )
