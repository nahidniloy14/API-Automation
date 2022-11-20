import requests
from behave import *

from SQL.IntegrateDatabaseUsingAPI.payloadDB import *
from Utilities.configuration import *
from Utilities.resources import *


@given(
    "The book details which needs to be added to library")  # this tag will look for given and execute if the string matches
# context will the variable act like a property. So that we can use it in every scenario
def step(context):
    context.url = getConfig()["API"]["endpoint"] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payload = buildPayloadFromDB("dummy")


@when(u'We execute post method')
def step_impl(context):
    context.addBook_response = requests.post(context.url, json=context.payload, headers=context.headers)
    #name should be same for all scenario such as context.response
# @when(u'We execute post method')
# def step_impl(context):
#     context.response = requests.post(context.url, json=context.payload, headers=context.headers)


@then(u'Book is suceessfully added')
def step_impl(context):
    print(context.addBook_response.json())
    json_response = context.addBook_response.json()
    context.bookID = json_response["ID"]
    print(context.bookID)
