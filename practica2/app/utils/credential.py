import json
from pickleshare import *


def set_token(email, password):
    return json.dumps({'email': email, 'password': password})


def get_token(token):
    return json.loads(token)


def login(email, password):
    db = PickleShareDB('~/testpickleshare')
    try:
        if not email or not password:
            return False

        if email not in db.keys():
            return False

        if db[email] != password:
            return False
        return True
    except:
        return False


def signup(email, password, repeat_password):
    db = PickleShareDB('~/testpickleshare')
    if not email or not password or password != repeat_password:
        return False

    if email in db.keys():
        return False

    db[email] = password
    return True
