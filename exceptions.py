class ServiceException(Exception):
    """
    Exception for Service class
    """
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return "\n ServiceException:\n\t%s" % self.__message


class MenuException(Exception):
    """
    Exception for Menu class
    """
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return "\n MenuException:\n\t%s" % self.__message
