
class User(object):
    """
    User entity of the marketplace
    """

    def __init__(self, username) -> None:
        super().__init__()
        self.username = username

    def __repr__(self) -> str:
        return "{}".format(self.username)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.username.lower() == other.username.lower()
        return False

    def __hash__(self) -> int:
        return hash(self.username.lower())
