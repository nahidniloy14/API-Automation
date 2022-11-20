import requests
from behave import *

from Utilities.resources import ApiResources


@given('I have github auth credentials')
def step(context):
    context.Gitsession = requests.session()
    context.Gitsession.auth = auth = ("nahidniloy14", "1414")

@when('I hit the getRepo API of github')
def step(context):
    context.Response = context.Gitsession.get(ApiResources.gitRepo)


@then('status code should be {statuscode:d}')#:d to mark it is an integar
def step(context,statuscode):
    print(context.Response.status_code)
    assert context.Response==statuscode
