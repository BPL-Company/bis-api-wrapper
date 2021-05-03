from .auth import Auth


class User:
    def __init__(self, user):
        self.id = user['_id']
        self.nickname = user['nickname']
        self.nicknames = user['nicknames']
        self.auth = Auth(user['auth'])
        self.role = user['role']
        self.connected_to = user['connected_to']
        self.money = user['money']
