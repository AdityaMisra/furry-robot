from typing import List

from command_handlers.handler import CommandHandlerInterface
from entity.category import Category
from entity.listing import Listing
from entity.user import User


class CreateListingHandler(CommandHandlerInterface):

    def handle(self, parameters: str) -> str:

        params = self.parse_input(parameters)

        username = params[0]
        if not self.authenticate(username):
            return self.error_unknown_user

        title = params[1]
        description = params[2]
        price = float(params[3])
        category_name = params[4]

        return self.create_listing(title, description, price, username, category_name)

    def create_listing(self, title: str, description: str, price: float, username: str, category_name: str) -> str:
        """
        Creates entry for the listing in marketplace and updates the category
        :param title: title of the listing
        :param description: description of the listing
        :param price: price of the listing
        :param username: username of the listing
        :param category_name: category of the listing
        :return: listing id
        """

        listing = Listing(self._generate_id(), title, description, price, User(username), category_name)

        # update listing in the marketplace
        self.marketplace.listings.update({listing.id: listing})

        # if listing's category doesn't exists then create a category
        category = self.marketplace.categories.get(listing.category_name)
        if not category:
            self.marketplace.categories[listing.category_name] = Category(category_name)

        # update listing in the marketplace's category
        self.marketplace.categories[listing.category_name].add_listing(listing)

        # calculating the top_category
        self.marketplace.top_category_name = max(self.marketplace.categories,
                                                 key=lambda key: len(self.marketplace.categories[key].listings))

        return str(listing.id)

    def _generate_id(self) -> int:
        """
        Generates the id for the listing.
        :return: id
        """

        get_id = lambda l: 100000 + l

        return get_id(len(self.marketplace.listings) + 1)

    def parse_input(self, parameters: str) -> List:
        params = []
        for each_param in parameters.split("'"):
            _each_param = each_param.strip()
            if not _each_param:
                continue
            params.append(_each_param)

        return params
