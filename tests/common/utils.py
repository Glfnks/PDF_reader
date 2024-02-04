import os

from dotenv import load_dotenv

env = os.environ
load_dotenv()


def get_main_path():
    """
        Find file in project and return path to it
    :return: main path
    """

    return os.getcwd()
