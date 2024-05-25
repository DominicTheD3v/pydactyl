import requests
from ..auth import Session
from ..debug import InvalidRequestMethodError

class Request():
    def __init__(self, session: Session, endpoint: str, method: str, data: dict = None, headers: dict = None):
        self.session = session
        self.method = method
        self.data = data
        self.headers = headers
        self.endpoint = endpoint
        
    def send(self):
        r = None
        if self.headers == None:
            self.headers = {"Authorization": "Bearer " + self.session.api_key}
        else:
            self.headers["Authorization"] = "Bearer " + self.session.api_key
            
        match self.method.lower():
            case "get":
                print("get")
                r = requests.get(url=self.endpoint, headers=self.headers, data=self.data)
                return r
            case "post":
                print("post")
                r = requests.post(url=self.endpoint, headers=self.headers, data=self.data)
                return r
            case "put":
                print("put")
                r = requests.put(url=self.endpoint, headers=self.headers, data=self.data)
                return r
            case "delete":
                print("delete")
                r = requests.delete(url=self.endpoint, headers=self.headers, data=self.data)
                return r
            case _:
                raise InvalidRequestMethodError
                 