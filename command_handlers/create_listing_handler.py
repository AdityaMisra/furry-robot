from typing import List

from command_handlers.handler import CommandHandlerInterface
from entity.category import Category
from entity.listing import Listing
from entity.user import User


class CreateListingHandler(CommandHandlerInterface):
    error_unknown_user = "Error - unknown user"

    def handle(self, parameters: str) -> str:

        params = self.parse_input(parameters)

        username = params[0]
        if not self.authenticate(username):
            return self.error_unknown_user

        title = params[1]
        description = params[2]
        price = float(params[3])
        category_name = params[4]

        listing = Listing(self._generate_id(), title, description, price, User(username),
                          category_name)

        self.marketplace.listings.update({listing.listing_id: listing})

        category = self.marketplace.categories.get(listing.category_name)
        if not category:
            self.marketplace.categories[listing.category_name] = Category(category_name)

        self.marketplace.categories[listing.category_name].add_listing(listing)

        self.marketplace.top_category_name = max(self.marketplace.categories,
                                                 key=lambda key: len(self.marketplace.categories[key].listings))

        return str(listing.listing_id)

    def _generate_id(self):
        _id = lambda l: 100000 + l

        return _id(len(self.marketplace.listings) + 1)

    def parse_input(self, parameters: str) -> List:
        params = []
        for each_param in parameters.split("'"):
            _each_param = each_param.strip()
            if not _each_param:
                continue
            params.append(_each_param)

        return params
