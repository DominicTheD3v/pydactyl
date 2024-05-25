class User():
    def __init__(self, username: str, email: str, first_name: str, last_name: str, admin: bool = False, password: str = ""):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.admin = admin
        self.password = password
