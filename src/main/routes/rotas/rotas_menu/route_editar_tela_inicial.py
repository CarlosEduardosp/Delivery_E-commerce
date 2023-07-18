from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_editar_tela_inicial = Blueprint("rota_editar_tela_inicial", __name__)


@api_routes_bp_editar_tela_inicial.route(
    "/editar_tela_inicial/<apelido>/<quantidade_carrinho>", methods=["GET", "POST"]
)
def editar_tela_inicial(apelido: str, quantidade_carrinho: int):
    """editar imagem da tela inicial"""

    if request.method == "POST":
        imagem = request.files.get("upload")

        if imagem:
            # adquirindo nome do arquivo do upload
            nome_imagem = imagem.filename

            # salvando arquivo na pasta static.
            diretorio = "./src/main/configs/static/imagem"
            imagem.save(os.path.join(diretorio, nome_imagem))

            imagem = AdapterImagem(
                api_route=register_imagem_composer(), data={"imagem": nome_imagem}
            )
            response = imagem.select()

            if response.status_code == 200:
                response = response.body
                response = response.imagem

                # deletando a imagem antiga do banco
                imagem.delete()

                # deletando a imagem da pasta /static/imagem
                if nome_imagem != response:
                    path = f"./src/main/configs/static/imagem/{response}"
                    os.remove(path)

            # inserindo a imagem nova no banco
            imagem.insert()

            return render_template(
                "editar_tela_inicial.html",
                apelido=apelido,
                quantidade_carrinho=quantidade_carrinho,
                imagem=nome_imagem,
            )

    return render_template(
        "editar_tela_inicial.html",
        apelido=apelido,
        quantidade_carrinho=quantidade_carrinho,
    )
