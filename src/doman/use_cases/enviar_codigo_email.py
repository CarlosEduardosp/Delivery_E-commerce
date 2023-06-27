from abc import ABC, abstractmethod


class EnviarCodigoEmail(ABC):
    """Interface to buscarcep Use case"""

    @abstractmethod
    def enviar_email_codigo(self, codigo: int, email_destinatario: str) -> bool:
        """
        envio de email com o codigo de validação, para cadastrar.
        """

        raise Exception("Should implement method: register")
