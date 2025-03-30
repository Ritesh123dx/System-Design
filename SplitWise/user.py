import uuid


class User:
    def __init__(self, name : str, email : str) -> None:
        self.name = name
        self.email = email
        self.id = str(uuid.uuid4())
