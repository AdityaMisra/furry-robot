from typing import List

from command_handlers.handler import CommandHandlerInterface
from entity.listing import Listing
from entity.user import User


class DeleteListingHandler(CommandHandlerInterface):
    error_listing_mismatch = "Error - listing owner mismatch"
    error_listing_does_not_exist = "Error - listing does not exist"

    def handle(self, parameters: str) -> str:

        params = self.parse_input(parameters)
        username = params[0]

        listing_id = int(params[1])
        listing = self.marketplace.listings.get(listing_id)
        if not listing:
            return self.error_listing_does_not_exist

        if listing.user != User(username):
            return self.error_listing_mismatch

        return self.delete_listing(listing)

    def delete_listing(self, listing: Listing) -> str:
        """
        Deletes the listing from the marketplace
        :param listing: Listing instance
        :return: Success message after successfully deleting it
        """

        # remove listing from the marketplace
        self.marketplace.listings.pop(listing.id, None)

        # remove listing from the category
        self.marketplace.categories[listing.category_name].remove_listing(listing)

        # after removing listing from the category, check if a category doesn't have any listings,
        # then remove the category as well
        if len(self.marketplace.categories[listing.category_name].listings) == 0:
            self.marketplace.categories.pop(listing.category_name)

        # calculating the top_category
        if self.marketplace.categories:
            self.marketplace.top_category_name = max(self.marketplace.categories,
                                                     key=lambda key: len(self.marketplace.categories[key].listings))
        else:
            self.marketplace.top_category_name = None

        return self.success

    def parse_input(self, parameters: str) -> List:
        params = parameters.split(' ')

        return params
