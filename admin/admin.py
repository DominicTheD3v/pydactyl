from ..auth import Session
from ..users import User
from ..utils import Request

class Users():
    def __init__(self, session: Session):
        self.session = session
        
    def create(self, user: User):
        data = {
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "password": user.password,
            "username": user.username,
            "root_admin": user.admin
        }
        
        r = Request(session=self.session, endpoint=self.session.panel_url + "/api/application/users/", method="POST", data=data, headers=None).send()
        return r