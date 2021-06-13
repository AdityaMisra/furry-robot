from typing import List

from entity.user import User
from service.marketplace import MarketPlace


class CommandHandlerInterface:
    success = 'Success'
    error_unknown_user = "Error - unknown user"

    def __init__(self) -> None:
        super().__init__()
        self.marketplace = MarketPlace()

    def handle(self, parameters: str) -> str:
        """
        Handles the requested command. Every new command needs to override this method
        :param parameters: command in string format
        :return: response of the command after processing
        """
        pass

    def parse_input(self, parameters: str) -> List:
        """
        Parse the command to extract the input parameters
        :param parameters: string
        :return: list of the input parameters
        """
        pass

    def authenticate(self, username: str) -> bool:
        """
        Authenticates the username passed in the command
        :param username: user's name
        :return: True if user is present in the system
        """
        return User(username) in self.marketplace.users
