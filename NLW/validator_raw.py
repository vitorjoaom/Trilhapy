from cerberus import Validator

body = {
    "data": {
        "elemento1": 123,
        "elemento2": "olaMundo",
        "elemento3": "123"
    }
}

body_Validator = Validator({
    "data": {
        "type": "dict",
        "schema": {
            "elemento1": {"type": "float", "reqired":True, "empty":False},
            "elemento2": {"type": "string", "required":False, "empty": False},
        }
    }
})

response = body_Validator.validate(body)

print(response)
print(body_Validator.errors)