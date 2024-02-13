from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import CreateTagController

class TagCreatorView:
    '''
        responsability for intercting with HTTP
    '''

    def validate_and_create(self, http_request: HttpRequest):
        tag_creator_controller = TagCreatorController()
        
        body = http_request.body
        product_code = body["product_code"]

        #logica de regra de negocio
        formated_response = tag_creator_controller.create(product_code)
        #retorno http
        return HttpResponse(status_code=200, body=formated_response)