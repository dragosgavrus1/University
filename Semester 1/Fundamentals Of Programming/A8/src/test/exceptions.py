class IdException(Exception):
    def __init__(self, message):
        self.message = message


class CommandException(Exception):
    def __init__(self, message):
        self.message = message
