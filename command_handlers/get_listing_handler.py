from command_handlers.handler import CommandHandlerInterface


class GetListingHandler(CommandHandlerInterface):
    error_not_found = "Error - not found"

    def handle(self, parameters: str) -> str:

        params = self.parse_input(parameters)

        username = params[0]
        if not self.authenticate(username):
            return self.error_unknown_user

        listing_id = int(params[1])

        return self.get_listing(listing_id)

    def get_listing(self, listing_id: int) -> str:
        """
        Fetch the listing from the marketplace
        :param listing_id: listing's id
        :return: Listing instance
        """

        listing = self.marketplace.listings.get(listing_id)
        if listing:
            return listing

        return self.error_not_found

    def parse_input(self, parameters):
        return parameters.split(' ')
