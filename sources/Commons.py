# coding: utf-8


import traceback
from logging import getLogger, config


config.fileConfig("./logging.conf")
logger = getLogger()


def print_line():
    print("----------------------------------------------------------------------------")


class NoLogsException(Exception):
    pass


def log(func):
    def wrapper(obj, *args, **kwds):
        try:
            logger.debug("  START  {}  args={} kwds={}".format(func.__name__, args, kwds))
            rtn = func(obj, *args, **kwds)
            logger.debug("    END  {}  return={}".format(func.__name__, rtn))
            return rtn

        except NoLogsException as error:
            raise error

        except Exception as error:
            logger.error(traceback.format_exc())
            logger.debug("    END  {}".format(func.__name__))
            raise error

    return wrapper
