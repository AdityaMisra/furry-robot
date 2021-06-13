from typing import List

from command_handlers.handler import CommandHandlerInterface


class GetTopCategoryHandler(CommandHandlerInterface):
    error_unknown_user = "Error - unknown user"

    def handle(self, parameters: str) -> str:

        username = self.parse_input(parameters)[0]
        if not self.authenticate(username):
            return self.error_unknown_user

        return self.marketplace.top_category_name

    def parse_input(self, parameters: str) -> List:
        return parameters.split(' ')
