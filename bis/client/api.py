from requests import get
from bis.exceptions import ServerError


class Api:
    def __init__(self, token, url):
        self.url = url
        self.token = token

    def make_request(self, method, params=None):
        if params is None:
            params = {}
        params.update({'auth_token': self.token})
        answer = get(self.url+method, params=params)
        try:
            return answer.json()
        except:
            raise ServerError('автор шиз получил ошибку на сервере и он упал)')

    def get_auth_token(self):
        return self.make_request('get_auth_token')

    def get_user_by_id(self, user_id):
        return self.make_request(f'get_user_by_id/{user_id}')

    def get_user_by_tg_id(self, tg_id):
        return self.make_request(f'get_user_by_tg_id/{tg_id}')

    def get_user_by_nickname(self, nickname):
        return self.make_request(f'get_user_by_nickname/{nickname}')

    def merge_users(self, **kwargs):
        return self.make_request(f'merge_users', kwargs)

    def create_user(self, **kwargs):
        return self.make_request(f'create_user', kwargs)

    def create_tg_user(self, **kwargs):
        return self.make_request(f'create_tg_user', kwargs)

    def create_minecraft_user(self, **kwargs):
        return self.make_request(f'create_minecraft_user', kwargs)

    def add_connection(self, **kwargs):
        return self.make_request(f'add_connection', kwargs)

    def add_auth(self, **kwargs):
        return self.make_request(f'add_auth', kwargs)

    def update_nickname(self, **kwargs):
        return self.make_request(f'update_nickname', kwargs)

    def remove_nickname(self, **kwargs):
        return self.make_request(f'remove_nickname', kwargs)

    def set_money(self, **kwargs):
        return self.make_request(f'set_money', kwargs)

    def inc_money(self, **kwargs):
        return self.make_request(f'inc_money', kwargs)

    def dec_money(self, **kwargs):
        return self.make_request(f'dec_money', kwargs)
