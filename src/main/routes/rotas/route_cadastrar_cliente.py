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

        # realizando a pesquisa do cep.
        if cep_cliente:
            endereco = BuscarCep(
                api_route=buscar_cep_composer(), data={"cep_cliente": cep_cliente}
            )
            endereco = endereco.adapter_buscar_cep()
            endereco = endereco.body

            # se o usuario digitar algum complemento.
            if complemento:
                session["complemento"] = complemento
            else:
                session["complemento"] = endereco.complemento

        # comparação das senhas e retorna um valor boolean
        if senha and confirmar_senha:
            response_senha = validador_senha(senha, confirmar_senha)

            if not response_senha:
                flash("erro -- senhas não conferem !!")

            else:
                # registrar codigo no banco
                faker = Faker()
                codigo = faker.random_number(digits=4)
                enviar_codigobd = AdapterCodigo(
                    api_route=register_codigo_composer(),
                    data={"codigo": codigo, "id_cliente": 1},
                )
                enviar_codigobd.insert()

                enviar_codigo = EnviarCodigoEmail()
                enviar_codigo.enviar_email_codigo(
                    codigo=codigo, email_destinatario=email
                )

                dados_cliente = Cliente(
                    id_cliente=0,
                    apelido=apelido,
                    email=email,
                    senha=senha,
                    cep_cliente=cep_cliente,
                )

                # guardando os dados do cliente
                session["dados_cliente"] = dados_cliente
                session["endereco_cliente"] = endereco

                return render_template(
                    "validacao_codigo.html", email=email, apelido=apelido
                )

    return render_template(
        "cadastrar_cliente.html", email=email, apelido=apelido, endereco=endereco
    )
