from .tag_creator_validator import tag_Creator_validator
from src.errors.error_types.http_unprocessable_entity import HttpProcessableEntityError

class MockRequest:
    def __init__(self) -> None:
        self.json = json

def test_creator_validator(): 
    req = MockRequest(json={"product_code": "12345"})
    tag_Creator_validator(req)

def test_tag_creator_validator_with_error():
    req = MockRequest(json={"product_code": "12345"})
    
    try:
        tag_Creator_validator(req)
    except Exception as exception:
        assert isinstance(exception, HttpProcessableEntityError)