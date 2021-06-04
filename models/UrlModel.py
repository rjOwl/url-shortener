from mongoengine import MapField, EmbeddedDocumentField, Document, ListField, StringField, EmbeddedDocument, DictField
import mongoengine as db
from flask import jsonify
from pymongo.read_preferences import Primary
from helpers.helpers import *

# Schema
'''
slug: "s5G1f3"
ios:
  primary: "http://..."
  fallback: "http://..."
android:
  primary: "http://..."
  fallback: "http://..."
web: "http://..."
'''

# class ios(EmbeddedDocument):
#   primary = StringField(required=True)
#   fallback = StringField(required=True)

# class android(EmbeddedDocument):
#   primary = StringField(required=True)
#   fallback = StringField(required=True)

class ShortenedUrl(Document):
    slug = StringField(unique=True, required=False, max_length=70)
    ios = DictField(required=True)
    android = DictField(required=True)
    # ios = MapField(EmbeddedDocumentField(ios))
    # android = MapField(EmbeddedDocumentField(android))
    web = StringField(required=True)


# connectionString = "mongodb+srv://team7-ninjas:123intake41@goodbookscluster.mrby6.mongodb.net/shortenedURLSDB?retryWrites=true&w=majority"
# if db.connect(host=connectionString):
# print("Connected to Atlas DB")


# url = ShortenedURL(
#         slug='asdj79', 
#         ios={"primary":"ios_prim", "fallback":"ios_fallback"},
#         android={"primary":"android_prim", "fallback":"android_fallback"},
#         web="http")
# try:
#   url.save()
# except db.errors.NotUniqueError as e:
#   print("Not unique")

# for i in ShortenedURL.objects:

