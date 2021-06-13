from pprint import pprint

from command_handlers.command_factory import factory


def input_parser(params):
    commands = params.split(' ', 1)
    command_handler = factory.get_command_handler(commands[0])

    if not command_handler:
        return "Invalid Command"

    output = command_handler.handle(commands[1])

    # For debugging
    # pprint(command_handler.marketplace.__dict__)

    return output


def reader():
    while True:
        try:
            print(input_parser(input("# ")))
        except EOFError as e:
            exit(0)


if __name__ == '__main__':
    reader()
