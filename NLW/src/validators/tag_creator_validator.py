from cerberus import Validator
from src.errors.error_types.http_unprocessable_entity import HttpProcessableEntityError

'''
{
    "product_code: 123"
}
'''

def tag_Creator_validator(request: any) -> None:
    body_Validator = Validator({
        "product_code":{"type": "string", "required": True, "empty": False}
    })

    response = body_Validator.validate(request.json)
    if response is False:
        raise HttpProcessableEntityError(body_Validator.errors)
    else:
        print("Ok!")