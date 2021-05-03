from .api import Api
from ..models import User, Response
from ..exceptions import ExceptionManager


class Client:
    def __init__(self, token, url):
        self.api = Api(token, url)
        self.exceptions = ExceptionManager()

    def get_auth_token(self):
        return self.api.get_auth_token()['result']

    def get_user_by_id(self, user_id):
        response = Response(self.api.get_user_by_id(user_id=user_id))
        if not response.ok:
            self.exceptions.raise_exception(response.errcode, response.reason)
        user = User(response.result)
        return user

    def get_user_by_nickname(self, nickname):
        response = Response(self.api.get_user_by_nickname(nickname=nickname))
        if not response.ok:
            self.exceptions.raise_exception(response.errcode, response.reason)
        user = User(response.result)
        return user

    def create_user(self, nickname, auth_string, auth_method):
        response = Response(self.api.create_user(nickname=nickname, auth_string=auth_string, auth_method=auth_method))
        if not response.ok:
            self.exceptions.raise_exception(response.errcode, response.reason)
        new_user = User(response.result)
        return new_user

    def create_tg_user(self, nickname, tg_id):
        response = Response(self.api.create_tg_user(nickname=nickname, tg_id=tg_id))
        if not response.ok:
            self.exceptions.raise_exception(response.errcode, response.reason)
        new_user = User(response.result)
        return new_user

    def create_minecraft_user(self, nickname):
        response = Response(self.api.create_minecraft_user(nickname=nickname))
        if not response.ok:
            self.exceptions.raise_exception(response.errcode, response.reason)
        new_user = User(response.result)
        return new_user

    def add_connection(self, user_id, connection):
        response = Response(self.api.add_connection(user_id=user_id, connection=connection))
        if not response.ok:
            self.exceptions.raise_exception(response.errcode, response.reason)
        return response.ok

    def add_auth(self, user_id, auth_method, auth_string):
        response = Response(self.api.add_auth(user_id=user_id, auth_method=auth_method, auth_string=auth_string))
        if not response.ok:
            self.exceptions.raise_exception(response.errcode, response.reason)
        return response.ok

    def update_nickname(self, user_id, nickname):
        response = Response(self.api.update_nickname(user_id=user_id, nickname=nickname))
        if not response.ok:
            self.exceptions.raise_exception(response.errcode, response.reason)
        return response.ok

    def remove_nickname(self, user_id, nickname):
        response = Response(self.api.remove_nickname(user_id=user_id, nickname=nickname))
        if not response.ok:
            self.exceptions.raise_exception(response.errcode, response.reason)
        return response.ok

    def set_money(self, user_id, count):
        response = Response(self.api.set_money(user_id=user_id, count=count))
        if not response.ok:
            self.exceptions.raise_exception(response.errcode, response.reason)
        return response.ok

    def inc_money(self, user_id, count):
        response = Response(self.api.inc_money(user_id=user_id, count=count))
        if not response.ok:
            self.exceptions.raise_exception(response.errcode, response.reason)
        return response.ok

    def dec_money(self, user_id, count):
        response = Response(self.api.dec_money(user_id=user_id, count=count))
        if not response.ok:
            self.exceptions.raise_exception(response.errcode, response.reason)
        return response.ok
