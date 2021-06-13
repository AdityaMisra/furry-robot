from datetime import datetime

from entity.user import User


class Listing(object):
    """
    Listing entity of the marketplace
    """

    def __init__(self, id: int, title: str, description: str, price: float, user: User, category_name: str) -> None:
        super().__init__()
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.user = user
        self.category_name = category_name
        self.creation_time = datetime.now()

    def __repr__(self) -> str:
        return "{0}|{1}|{2}|{3}|{4}|{5}".format(self.title, self.description, int(self.price),
                                                self.creation_time.strftime('%Y-%m-%d %H:%M:%S'), self.category_name,
                                                self.user)
