from typing import List

from entity.user import User
from service.marketplace import MarketPlace


class CommandHandlerInterface:
    success = 'Success'

    def __init__(self) -> None:
        super().__init__()
        self.marketplace = MarketPlace()

    def handle(self, parameters: str) -> str:
        """

        :param parameters:
        :return:
        """
        pass

    def parse_input(self, parameters: str) -> List:
        """

        :param parameters:
        :return:
        """
        pass

    def authenticate(self, username):
        """

        :param username:
        :return:
        """
        return User(username) in self.marketplace.users
