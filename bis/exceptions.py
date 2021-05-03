class ExceptionManager:
    def __init__(self):
        self.exceptions = {
            -2: InvalidToken,
            -1: MissingToken,
            0: MissingArgs,
            1: UsedNickanme,
            2: UsedAuth,
            3: UserNotFound,
            4: AuthNotFound,
            5: NicknameNotFound
        }

    def raise_exception(self, errcode, reason):
        raise self.exceptions.get(errcode, BISException)(reason)


class BISException(Exception):
    def __init__(self, text):
        Exception.__init__(self, text)


class InvalidToken(BISException):
    def __init__(self, text):
        BISException.__init__(self, text)


class MissingToken(BISException):
    def __init__(self, text):
        BISException.__init__(self, text)


class MissingArgs(BISException):
    def __init__(self, text):
        BISException.__init__(self, text)


class UsedNickanme(BISException):
    def __init__(self, text):
        BISException.__init__(self, text)


class UsedAuth(BISException):
    def __init__(self, text):
        BISException.__init__(self, text)


class UserNotFound(BISException):
    def __init__(self, text):
        BISException.__init__(self, text)


class AuthNotFound(BISException):
    def __init__(self, text):
        BISException.__init__(self, text)


class NicknameNotFound(BISException):
    def __init__(self, text):
        BISException.__init__(self, text)


class ServerError(BISException):
    def __init__(self, text):
        BISException.__init__(self, text)
