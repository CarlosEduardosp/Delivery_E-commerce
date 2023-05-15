from .cliente_repository_interface import ClienteRepositoryInterface
from .endereco_repository_interface import EnderecoRepositoryInterface
from .carrinho_repository_interface import CarrinhoRepositoryInterface
from .codigo_repository_interface import CodigoRepositoryInterface
from .imagem_repository_interface import ImagemPerfilRepositoryInterface
from .pedido_repository_interface import PedidoRepositoryInterface
from .produto_repository_interface import ProdutoRepositoryInterface

print(
    CarrinhoRepositoryInterface,
    ClienteRepositoryInterface,
    EnderecoRepositoryInterface,
    CodigoRepositoryInterface,
    ImagemPerfilRepositoryInterface,
    PedidoRepositoryInterface,
    ProdutoRepositoryInterface,
)
