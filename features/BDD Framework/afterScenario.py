import requests

from Utilities.configuration import getConfig
from Utilities.resources import ApiResources


def after_scenario(context,scenario):
    url2 = getConfig()["API"]["endpoint"] + ApiResources.deleteBook
    deleteBook = requests.post(url2, json={"ID": context.bookID})


