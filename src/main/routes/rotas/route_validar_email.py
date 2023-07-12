from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_validar = Blueprint("validar_email", __name__)


@api_routes_bp_validar.route("/validar/<email>", methods=["GET", "POST"])
def validar_email(email: str):
    """validar o codigo enviado para o email"""

    # request do valor do codigo via form
    if request.method == "POST":
        codigo = request.form.get("codigo")
        if codigo:
            # validação do codigo, com o codigo cadastrado
            response = comparar_codigo(codigo)
            if response:
                # salvando dados do cliente no banco
                cliente = session.get("dados_cliente")
                cliente_insert = AdapterCliente(
                    api_route=register_cliente_composer(),
                    data={
                        "apelido": cliente[1],
                        "email": cliente[2],
                        "senha": cliente[3],
                        "cep_cliente": cliente[4],
                    },
                )
                response_cliente = cliente_insert.insert()

                id_cliente = response_cliente.body.id_cliente

                # salvando endereço no banco
                complemento = session.get("complemento")
                endereco = session.get("endereco_cliente")
                insert_endereco = AdapterEndereco(
                    api_route=register_endereco_composer(),
                    data={
                        "id_cliente": id_cliente,
                        "cep_cliente": endereco[0],
                        "estado": endereco[1],
                        "cidade": endereco[2],
                        "bairro": endereco[3],
                        "logradouro": endereco[4],
                        "complemento": complemento,
                    },
                )
                insert_endereco.insert()

                # deletando do banco o codigo validado pelo cliente
                del_codigo = AdapterCodigo(
                    api_route=register_codigo_composer(),
                    data={"id_cliente": response_cliente.body.id_cliente},
                )
                del_codigo.delete()  # metodo para deletar o codigo no banco

                apelido = cliente[1]

                return redirect(
                    url_for("home.home", apelido=apelido, quantidade_carrinho=0)
                )

    return render_template(
        "validacao_codigo.html", email=email, apelido="Efetue_o_Login!"
    )
