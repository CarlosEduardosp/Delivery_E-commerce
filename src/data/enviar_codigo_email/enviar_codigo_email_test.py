from src.data.enviar_codigo_email.enviar_codigo import EnviarCodigoEmail
from faker import Faker

faker = Faker()


def test_enviar_codigo():
    enviar = EnviarCodigoEmail()
    response = enviar.enviar_email_codigo(
        faker.random_number(digits=4), "carlos.spadilha@yahoo.com.br"
    )
    print(response)
