from services import UrlService
from helpers.helpers import *
from flask import jsonify, Response


def get_urls(req):
    data = UrlService.get_urls()
    return data, 200

def create_short_url(req):
    data = req.json
    slug = generateSlug()
    if 'slug' in data:
        if data['slug']:
            slug = data['slug']
    print(data)

    return UrlService.create_short_url(data)

def edit_url(req, slug):
    body = req.json
    return UrlService.edit_url_body(body, slug)

