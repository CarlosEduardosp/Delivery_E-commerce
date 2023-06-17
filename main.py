from faker import Faker

faker = Faker()


class Pessoa:
    def __init__(self, nome: str, idade: int) -> dict[bool, None]:
        """método construtor classe Pessoa"""
        self.nome = nome
        self.idade = idade

    def somar(self):
        if self.__validar():
            return self.__somando()

        return self.__erro()

    def __somando(self):
        """calculo de somatorio"""
        return {"Success": True, "Data": self.idade + self.idade}

    def __validar(self):
        """validando dados"""
        validador = isinstance(self.idade, int)
        return {"Success": validador, "Data": validador}

    def __erro(self):
        """mensagem de erro"""
        return {"Success": False, "Data": "Valores referentes a idade estão incorretos"}


def somar(valor_1: int = 0, valor_2: int = 0, valor_3: int = 0) -> int:
    soma = valor_1 + valor_2 + valor_3
    return soma


testando = somar(12, 3)
print(testando)
