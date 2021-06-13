from typing import List

from command_handlers.handler import CommandHandlerInterface
from entity.user import User


class RegisterUserHandler(CommandHandlerInterface):
    error_user_already_exists = "Error - user already existing"

    def handle(self, parameters: str) -> str:

        params = self.parse_input(parameters)
        username = params[0]
        user = User(username)

        if user in self.marketplace.users:
            return self.error_user_already_exists

        return self.register_new_user(user)

    def register_new_user(self, user: User) -> str:
        """
        Add user to the marketplace user set
        :param user: user instance
        :return: Success message
        """

        self.marketplace.users.add(user)
        return self.success

    def parse_input(self, parameters: str) -> List:
        params = parameters.split(' ')

        if len(params) > 1:
            raise Exception("Invalid input parameters. Register 1 user at a time.")

        return params
