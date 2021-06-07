import logging

class Log():

    __instance = None
    __logger = None

    @staticmethod
    def getInstance():
        if Log.__instance == None:
            return Log()
            
        return Log.__instance

    def __init__(self):

        logging.basicConfig(format='%(asctime)s - %(name)s - %(process)s - %(levelname)s - %(message)s', level=logging.NOTSET)

        if Log.__instance != None:
            raise Exception("Can not instantiate more than once!")

        # Create a custom logger
        logger = logging.getLogger('symbl')

        # Create handlers
        c_handler = logging.StreamHandler()
        c_handler.setLevel(logging.NOTSET)

        self.__logger = logger
    
    def set_level(self, level):
        self.__logger.setLevel(level)

    def info(self, message: str, data=None):
        if data != None:
            self.__logger.info("{}, {}".format(message, data))
        else:
            self.__logger.info(message)

    def debug(self, data, *args):
        if args != None and len(args) > 0:
            self.__logger.debug(data, args[0])
        else:
            self.__logger.debug(data)

    def warning(self, data, *args):
        if args != None and len(args) > 0:
            self.__logger.warning(data, args[0])
        else:
            self.__logger.warning(data)
    
    def error(self, data, *args):
        if args != None and len(args) > 0:
            self.__logger.error(data, args[0])
        else:
            self.__logger.error(data)
