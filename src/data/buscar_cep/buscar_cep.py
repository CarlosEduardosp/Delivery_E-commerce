from src.doman.models_class_routes.endereco_cep_cliente import Endereco
from src.doman.use_cases.buscar_cep import BuscarCepInterface
import requests


class BuscarCep(BuscarCepInterface):
    """faz a busca com o cep e retorna, estado, cidade e etc."""

    __URL_API_VIACEP = "https://viacep.com.br/ws/{response}/json/"

    def pesquisar_cep(self, cep_cliente) -> Endereco:
        """Busca o endereço do usuário através do seu cep. com a Api do viacep."""

        validate_entry = isinstance(cep_cliente, str)
        if not validate_entry:
            return self.__error_str()

        response = cep_cliente.replace("-", "").replace(".", "").replace(" ", "")

        if len(response) == 8 and validate_entry:
            link = self.__URL_API_VIACEP.format(response=response)

            requisicao = requests.get(link)

            dic_requisicao = requisicao.json()

            if "erro" not in dic_requisicao:
                logradouro = dic_requisicao["logradouro"]
                complemento = dic_requisicao["complemento"]
                if not complemento:
                    complemento = "Complemente aqui..."
                uf = dic_requisicao["uf"]
                cidade = dic_requisicao["localidade"]
                bairro = dic_requisicao["bairro"]

                endereco = [uf, cidade, bairro, logradouro, complemento]
                response = Endereco(
                    cep_cliente=cep_cliente,
                    estado=endereco[0],
                    cidade=endereco[1],
                    bairro=endereco[2],
                    logradouro=endereco[3],
                    complemento=endereco[4],
                )
                return {"Success": True, "Data": response}
            else:
                return self.__error()
        else:
            return self.__error_len()

    def __error(self):
        """error"""

        return {"Success": False, "Data": "Cep Inválido !! Tente outra vez."}

    def __error_str(self):
        """error"""

        return {"Success": False, "Data": "Cep inválido, Precisa ser um string."}

    def __error_len(self):
        """error"""

        return {
            "Success": False,
            "Data": "Cep inválido, Precisa conter 8 numeros, em formato string.",
        }
