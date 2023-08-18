from src.main.routes.imports.imports_api_route import *  # noqa
import time

api_routes_bp_codigo = Blueprint("codigo", __name__)


@api_routes_bp_codigo.route("/codigo/<email>", methods=["GET", "POST"])
def codigo_validation(email: str):
    """gerar o codigo para validação do email"""

    # registrar codigo no banco
    faker = Faker()
    codigo = faker.random_number(digits=6)
    enviar_codigobd = AdapterCodigo(
        api_route=register_codigo_composer(),
        data={"codigo": codigo, "id_cliente": 1},
    )
    enviar_codigobd.insert()

    enviar_codigo = EnviarCodigoEmail()
    enviar_codigo.enviar_email_codigo(codigo=codigo, email_destinatario=email)

    session["codigo"] = True

    time.sleep(5)

    return redirect(
        url_for(
            "validar_email.validar_email",
            email=email,
            apelido="Efetue_o_Login!",
            quantidade_carrinho=0,
        )
    )
