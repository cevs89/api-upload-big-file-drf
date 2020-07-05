from cerberus import Validator


class ValidateObtaineToken():
    """
        {
        "username": "username",
        "password": "secrect_password"
        }
    """
    schema = {
        "username": {
            "type": "string",
            "required": True,
        },
        "password": {
            "type": "string",
            "required": True,
        }
    }

    def __init__(self, data):
        self.validator = Validator()
        self.data = data
        self.schema = self.__class__.schema

    def validate(self):
        return self.validator.validate(self.data, self.schema)

    def errors(self):
        return self.validator.errors


class ValidateChangePassword():
    """
        {
        "password": ""
        "password_confirm": ""
        }
    """
    schema = {
        "password": {
            "type": "string",
            "required": True,
            "maxlength": 100,
            "minlength": 6,
        },
        "password_confirm": {
            "type": "string",
            "required": True,
            "maxlength": 100,
            "minlength": 6,
        }
    }

    def __init__(self, data):
        self.validator = Validator()
        self.data = data
        self.schema = self.__class__.schema

    def validate(self):
        return self.validator.validate(self.data, self.schema)

    def errors(self):
        return self.validator.errors


class UserProfileValidator():
    """
        {
        "email": "email_valid",
        "first_name": "first_name"
        "last_name": "last_name"
        }
    """
    schema = {
        "email": {
            "type": "string",
            "required": False,
            "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
            "maxlength": 254
        },
        "first_name": {
            "type": "string",
            "required": False,
            "maxlength": 30,
        },
        "last_name": {
            "type": "string",
            "required": False,
            "maxlength": 150,
        }
    }

    def __init__(self, data):
        self.validator = Validator()
        self.data = data
        self.schema = self.__class__.schema

    def validate(self):
        return self.validator.validate(self.data, self.schema)

    def errors(self):
        return self.validator.errors
