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

    if not set(["ios", "android"]).issubset(data):
        print("1")
        return Response(status=400)
    else:
        if not set(["primary", "fallback"]).issubset(data['ios']):
            print("2")
            return Response(status=400)
        else:
            if not data["ios"]["primary"] or not data["ios"]["fallback"]:
                print("3")
                return Response(status=400)

        if not set(["primary", "fallback"]).issubset(data['android']):
            return Response(status=400)
        else:
            if not data["ios"]["primary"] or not data["ios"]["fallback"]:
                return Response(status=400)

    return UrlService.create_short_url(data)

def edit_url(req, slug):
    body = req.json
    return UrlService.edit_url_body(body, slug)

