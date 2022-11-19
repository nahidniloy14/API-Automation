import requests
from behave import *

from SQL.IntegrateDatabaseUsingAPI.payloadDB import *
from Utilities.configuration import *
from Utilities.resources import *


@given("The book details with {isbn} {aisle}")  # this tag will look for given and execute if the string matches
# context will the variable act like a property. So that we can use it in every scenario
def step(context,isbn,aisle):
    context.url = getConfig()["API"]["endpoint"] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payload = buildPayloadFromDB("dummy")

