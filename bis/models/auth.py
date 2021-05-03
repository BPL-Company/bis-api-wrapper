class Auth:
    def __init__(self, auth):
        self.telegram_id = auth['telegram_id']
        self.email = auth['email']
        self.phone_number = auth['phone_number']
        self.minecraft = auth['minecraft']
