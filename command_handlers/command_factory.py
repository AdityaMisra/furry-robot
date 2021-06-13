from command_handlers.create_listing_handler import CreateListingHandler
from command_handlers.delete_listing_handler import DeleteListingHandler
from command_handlers.get_category_handler import GetCategoryHandler
from command_handlers.get_listing_handler import GetListingHandler
from command_handlers.get_top_category_handler import GetTopCategoryHandler
from command_handlers.handler import CommandHandlerInterface
from command_handlers.register_user_handler import RegisterUserHandler


class CommandFactory:
    handler_map = {
        'REGISTER': RegisterUserHandler(),
        'CREATE_LISTING': CreateListingHandler(),
        'GET_LISTING': GetListingHandler(),
        'GET_CATEGORY': GetCategoryHandler(),
        'GET_TOP_CATEGORY': GetTopCategoryHandler(),
        'DELETE_LISTING': DeleteListingHandler(),
    }

    @classmethod
    def get_command_handler(cls, command) -> CommandHandlerInterface:
        return cls.handler_map.get(command)


factory = CommandFactory()
