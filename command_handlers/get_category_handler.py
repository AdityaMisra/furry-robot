from typing import List

from command_handlers.handler import CommandHandlerInterface


class GetCategoryHandler(CommandHandlerInterface):
    error_category_not_found = "Error - category not found"
    error_unknown_user = "Error - unknown user"

    def handle(self, parameters: str) -> str:

        params = self.parse_input(parameters)
        username = params[0]
        if not self.authenticate(username):
            return self.error_unknown_user

        category_name = params[1]
        category = self.marketplace.categories.get(category_name)
        if not category:
            return self.error_category_not_found

        listings = category.listings

        sorting = params[2]
        ordering = params[3]

        self._sort(listings, sorting, ordering)

        return self.format_output(listings)

    @staticmethod
    def _sort(listings, sorting, order):
        reverse = True if order == 'dsc' else False

        if sorting == 'sort_price':
            listings.sort(key=lambda x: x.price, reverse=reverse)
        elif sorting == 'sort_time':
            listings.sort(key=lambda x: x.creation_time, reverse=reverse)

    @staticmethod
    def format_output(listings):
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
