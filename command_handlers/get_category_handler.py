from typing import List

from command_handlers.handler import CommandHandlerInterface
from entity.category import Category
from entity.listing import Listing


class GetCategoryHandler(CommandHandlerInterface):
    error_category_not_found = "Error - category not found"

    def handle(self, parameters: str) -> str:

        params = self.parse_input(parameters)
        username = params[0]
        if not self.authenticate(username):
            return self.error_unknown_user

        category_name = params[1]
        category = self.marketplace.categories.get(category_name)
        if not category:
            return self.error_category_not_found

        return self.get_listing(category, params[2], params[3])

    def get_listing(self, category: Category, sort_field: str, ordering: str) -> str:
        """
        Get the listing for a particular category
        :param category: category queried for
        :param sort_field: sort the listing on this field - {sort_price or sort_time}
        :param ordering: order of the sorting - {asc or dsc}
        :return: sorted listing for a category in string format
        """

        listings = category.listings

        self._sort(listings, sort_field, ordering)

        return self.format_output(listings)

    @staticmethod
    def _sort(listings: List[Listing], sort_field: str, order: str) -> None:
        """
        Sort the list in place
        :param listings: List of listings(products)
        :param sort_field: sort the listing on this field - {sort_price or sort_time}
        :param order: order of the sorting - {asc or dsc}
        :return: None
        """

        reverse = True if order == 'dsc' else False

        if sort_field == 'sort_price':
            listings.sort(key=lambda x: x.price, reverse=reverse)
        elif sort_field == 'sort_time':
            listings.sort(key=lambda x: x.creation_time, reverse=reverse)

    @staticmethod
    def format_output(listings: List[Listing]) -> str:
        """
        Format the sorted listing
        :param listings: List of listings(products)
        :return: string
        """

        return "\n".join(map(str, listings))

    def parse_input(self, parameters: str) -> List:
        params = []

        for idx, each_param in enumerate(parameters.split("'")):
            _each_param = each_param.strip()
            if not _each_param:
                continue

            if idx == 2:
                params.extend(_each_param.split(' '))
            else:
                params.append(_each_param)

        return params
