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

        self._compute_top_category(listing.category_name)

        return self.success

    def _compute_top_category(self, listing_category_deleted: str) -> None:
        """
        Computes the top category in the marketplace after deleting a listing
        :param listing_category_deleted: deleted listing's category
        :return: None
        """

        # if not category is present then no need to compute the top category
        if not self.marketplace.categories:
            self.marketplace.top_category_name = None
            self.marketplace.top_category_listing_count = 0
            return None

        new_top_category_name = None

        # calculating the top_category if the deleted listing's category is same as top_category
        if listing_category_deleted == self.marketplace.top_category_name:
            new_top_category_name = max(self.marketplace.categories,
                                        key=lambda key: len(self.marketplace.categories[key].listings))
            self.marketplace.top_category_listing_count -= 1

        # newly computed top category's listing count is same as old top_category's listing count
        # then we don't update the old top_category
        if self.marketplace.categories[new_top_category_name] \
                and len(self.marketplace.categories[new_top_category_name].listings) == \
                self.marketplace.top_category_listing_count:
            return

        # update the top category
        self.marketplace.top_category_name = new_top_category_name

        # set the top_category's listing count
        self.marketplace.top_category_listing_count = len(
            self.marketplace.categories[self.marketplace.top_category_name].listings)

    def parse_input(self, parameters: str) -> List:
        params = parameters.split(' ')

        return params
