from entity.listing import Listing


class Category(object):
    """
    Category entity of the marketplace
    """

    def __init__(self, category_name) -> None:
        super().__init__()
        self.category_name = category_name
        self.listings = list()

    def __repr__(self) -> str:
        return "{}".format(self.category_name)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Category):
            return self.category_name == other.category_name
        return False

    def __hash__(self) -> int:
        return hash(self.category_name)

    def add_listing(self, listing: Listing) -> object:
        self.listings.append(listing)
        return self

    def remove_listing(self, listing: Listing) -> object:
        self.listings.remove(listing)
        return self
