from src.main.composer.buscar_cep_composer import buscar_cep_composer
from src.presenters.helpers.http_models import HttpRequest


http_request = HttpRequest(query={"cep_cliente": "28984350"})
response = buscar_cep_composer()
response = response.route_buscar_cep(http_request)

print(response)
