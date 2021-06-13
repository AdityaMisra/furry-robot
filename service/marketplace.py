from utils.singleton import Singleton


class MarketPlace(metaclass=Singleton):
    """
    Marketplace contains all the entities and their relationships
    """

    def __init__(self) -> None:
        self.top_category_name = None
        self.top_category_listing_count = 0
        self.users = set()

        """
            {
                category_name1: category1, 
                category_name2: category2
            }
        """
        self.categories = dict()

        """
            {
                listing_id1: listing1, 
                listing_id2: listing2
            }
        """
        self.listings = dict()
