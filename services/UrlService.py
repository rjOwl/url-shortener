from models.UrlModel import ShortenedUrl
from helpers.helpers import *
from flask import Response, jsonify
import mongoengine

def get_urls():
    data = ShortenedUrl.objects.to_json()
    print(data)
    return data


def create_short_url(body):
    slug = generateSlug()
    if 'slug' in body:
        if not body['slug']:
            body['slug'] = slug

    try:
        url = ShortenedUrl(
            slug=body["slug"],
            ios={"primary": body["ios"]["primary"], "fallback": body["ios"]["fallback"]}, 
            android={"primary": body["android"]["primary"],"fallback": body["android"]["fallback"]},
            web=body["web"]).save()
        return Response(status=200)
    except Exception as e:
        # if()
        # print(e)
        return {"error": "failed", "Status": 400}

def edit_url_body(body, slug):
    try:
        doc = ShortenedUrl.objects.get(slug=slug)
        for key, value in body.items():
            if key != "slug" and key in ["ios", "android"]:
                for embedKey, embedVal in body[key].items():
                    if embedKey in ["fallback", "primary"]:
                        # print(embedKey)
                        doc[key][embedKey] = body[key][embedKey]
        doc.save()
        return Response(status=201)
    except mongoengine.DoesNotExist as e:
        return Response(status=404)