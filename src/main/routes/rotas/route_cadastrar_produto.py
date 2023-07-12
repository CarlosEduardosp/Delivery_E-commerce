from src.main.routes.imports.imports_api_route import *  # noqa

api_routes_bp_cad_produto = Blueprint("rota_cadastrar_produto", __name__)


@api_routes_bp_cad_produto.route(
    "/cadastrar_produto/<apelido>/<quantidade_carrinho>/", methods=["GET", "POST"]
)
def cadastrar_produto(apelido: str, quantidade_carrinho: int):
    """endpoint para cadastrar produtos"""

    if request.method == "POST":
        nome_produto = request.form.get("nome")
        descricao = request.form.get("descricao")
        preco = request.form.get("preco")
        # recebendo post do arquivo para upload
        imagem = request.files.get("upload")

        # adquirindo nome do arquivo do upload
        nome_imagem = imagem.filename

        # salvando arquivo na pasta static.
        diretorio = "./src/main/configs/static/"
        imagem.save(os.path.join(diretorio, nome_imagem))

        # salvando os dados no banco
        cadastro_pro = AdapterProduto(
            api_route=register_produto_composer(),
            data={
                "nome": nome_produto,
                "descricao": descricao,
                "preco": float(preco),
                "imagem": nome_imagem,
            },
        )
        response = cadastro_pro.insert()
        if response.status_code == 200:
            return redirect(
                url_for(
                    "api_routes.cadastrar_produto",
                    apelido=apelido,
                    quantidade_carrinho=quantidade_carrinho,
                )
            )

    return render_template(
        "cadastrar_produto.html",
        apelido=apelido,
        quantidade_carrinho=quantidade_carrinho,
    )
