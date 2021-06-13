from utils.singleton import Singleton


class MarketPlace(metaclass=Singleton):
    """

    """

    def __init__(self) -> None:
        self.users = set()

        # {category_name: category}
        self.categories = dict()

        # {listing_id: listing}
        self.listings = dict()
        self.top_category_name = None
