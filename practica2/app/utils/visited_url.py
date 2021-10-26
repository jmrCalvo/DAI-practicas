from pickleshare import *
import json


def generate_stack(email):
    db = PickleShareDB('~/testpickleshare')
    try:
        db[email+'_url_last_visited'] = '/404*_*/404*_*/404'
        return True
    except:
        return False


def append_to_stack(request, url):
    user = request.cookies.get('user')
    if user == None:
        return False
    res = json.loads(user)
    email = res["email"]
    db = PickleShareDB('~/testpickleshare')
    try:
        last_urls = db[email+'_url_last_visited']
        url_arr = last_urls.split('*_*')
        url_arr.insert(0, url)
        last_urls_update = "*_*".join(url_arr)
        db[email+'_url_last_visited'] = last_urls_update
        return True
    except:
        return False


def get_stack(request):
    user = request.cookies.get('user')
    if user == None:
        return False
    res = json.loads(user)
    email = res["email"]
    db = PickleShareDB('~/testpickleshare')
    try:
        print('email', email)
        last_urls = db[email+'_url_last_visited']
        if last_urls != None:
            return last_urls.split('*_*')
        else:
            return ['/404', '/404', '/404']
    except:
        return ['/404', '/404', '/404']
