class Response:
    def __init__(self, response):
        self.ok = response['ok']
        self.result = response.get('result')
        self.errcode = response.get('errcode')
        self.reason = response.get('reason')
