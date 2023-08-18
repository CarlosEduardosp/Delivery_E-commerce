from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_cad_cliente = Blueprint("cadastrar_cliente", __name__)


@api_routes_bp_cad_cliente.route(
    "/cadastrar_cliente",
    defaults={"apelido": "Efetue_o_Login!"},
    methods=["GET", "POST"],
)
@api_routes_bp_cad_cliente.route(
    "/cadastrar_cliente/<apelido>", methods=["GET", "POST"]
)
def cadastrar_cliente(apelido: str):
    """tela de cadastro de cliente"""

    cep_cliente = ""
    endereco = ["---", "---", "---", "---", "---"]

    email = ""

    # request dos dados do usuario via formulario.
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        confirmar_senha = request.form.get("confirmar_senha")
        apelido = request.form.get("apelido")
        cep_cliente = request.form.get("end")
        complemento = request.form.get("complemento")
        estado = request.form.get("estado")
        cidade = request.form.get("cidade")
        bairro = request.form.get("bairro")
        logradouro = request.form.get("logradouro")
        complemento = request.form.get("complemento")

        # realizando a pesquisa do cep.
        if cep_cliente:
            endereco = BuscarCep(
                api_route=buscar_cep_composer(), data={"cep_cliente": cep_cliente}
            )
            response = endereco.adapter_buscar_cep()

            if response.status_code == 200:
                endereco = response.body
            else:
                flash(
                    "Não foi possivel realizar a consulta do cep, por favor coloque os dados manualmente."
                )

            # se o usuario digitar algum complemento.
            if complemento:
                session["complemento"] = complemento
            else:
                session["complemento"] = "complemente aqui..."

        # comparação das senhas e retorna um valor boolean
        if senha and confirmar_senha:
            response_senha = validador_senha(senha, confirmar_senha)

            if not response_senha:
                flash(
                    "Senhas não conferem !! Precisam ser iguais, e ter no mínimo 5 dígitos."
                )

            else:
                dados_cliente = Cliente(
                    id_cliente=0,
                    apelido=apelido,
                    email=email,
                    senha=senha,
                    cep_cliente=cep_cliente,
                )

                dados_endereco = Endereco(
                    id_endereco=0,
                    cep_cliente=cep_cliente,
                    estado=estado,
                    cidade=cidade,
                    bairro=bairro,
                    logradouro=logradouro,
                    complemento=complemento,
                    id_cliente=0,
                )

                # guardando os dados do cliente
                session["dados_cliente"] = dados_cliente
                if response.status_code == 200:
                    session["endereco_cliente"] = endereco
                else:
                    # salva os dados do endereço digitado no formulário pelo cliente
                    session["dados_endereco"] = dados_endereco

                return redirect(url_for("validar_email.validar_email", email=email))

    return render_template(
        "cadastrar_cliente.html",
        email=email,
        apelido=apelido,
        endereco=endereco,
        cep_cliente=cep_cliente,
    )
