from typing import List

from command_handlers.handler import CommandHandlerInterface
from entity.listing import Listing


class GetListingHandler(CommandHandlerInterface):
    error_not_found = "Error - not found"
    error_unknown_user = "Error - unknown user"

    def handle(self, parameters: str) -> str:

        params = self.parse_input(parameters)

        username = params[0]
        if not self.authenticate(username):
            return self.error_unknown_user

        listing_id = int(params[1])

        listing = self.marketplace.listings.get(listing_id)
        if listing:
            return listing

        return self.error_not_found

    def parse_input(self, parameters):
        return parameters.split(' ')
