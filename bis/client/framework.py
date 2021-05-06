from .client import Client
from bis.exceptions import *


class Framework:
    def __init__(self, token, url):
        self.client = Client(token, url)
        self.exceptions = ExceptionManager()

    def get_user_by_id(self, user_id):
        try:
            return self.client.get_user_by_id(user_id)
        except UserNotFound:
            return None

    def get_user_by_tg_id(self, tg_id):
        try:
            return self.client.get_user_by_tg_id(tg_id)
        except UserNotFound:
            return None
        except AuthNotFound:
            return None

    def create_user(self, nickname, auth_string, auth_method):
        try:
            return self.client.create_user(nickname, auth_string, auth_method)
        except UsedNickanme:
            return self.client.get_user_by_nickname(nickname)
        except UsedAuth:
            return None  # TODO: find by auth

    def create_tg_user(self, nickname, tg_id):
        try:
            return self.client.create_tg_user(nickname, tg_id)
        except UsedNickanme:
            return self.client.get_user_by_nickname(nickname)
        except UsedAuth:
            return None  # TODO: find by auth
