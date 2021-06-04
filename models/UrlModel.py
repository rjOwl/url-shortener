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
    web = StringField(required=True)
