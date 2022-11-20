import requests

from Utilities.configuration import getConfig
from Utilities.resources import ApiResources


def after_scenario(context,scenario):
    url2 = getConfig()["API"]["endpoint"] + ApiResources.deleteBook
    headers = {"Content-Type": "application/jsom"}
    context.deleteBook = requests.post(url2, json={"ID": context.bookID}, headers=headers)
    json_response = context.deleteBook.json()

    print(json_response["msg"])
    assert json_response["Msg"] == "successfully deleted"



