
class User:
    def __init__(self, username, password, name, user_id=None):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.name = name

    def set_id(self, user_id):
        self.user_id = user_id

    def check_password(self, password):
        if self.password == password:
            return True
        else:
            return False
