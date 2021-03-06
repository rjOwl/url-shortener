from flask import Flask, helpers, redirect, url_for, request, json, jsonify, Response
from werkzeug.wrappers import response
from controllers.UrlController import *
import boot.DBConnection
from flask_cors import CORS, cross_origin
from middlewares.ContentMiddleware import ContentMiddleware
from helpers.helpers import *

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# middleware
# app.wsgi_app = ContentMiddleware(app.wsgi_app)

# Return all shortend links with slug
@app.route('/shortlinks', methods = ['GET'])
@cross_origin()
def getShortendLinks():
    if not check_content_type(request.content_type):
        return Response(status=400)
    return get_urls(request)


@app.route('/shortlinks', methods = ['POST'])
@cross_origin()
def shortenLink():
    if not check_content_type(request.content_type):
        return Response(status=400)
    return create_short_url(request)


# Get the slug and edit the link
@app.route('/shortlinks/<slug>',methods = ['PUT'])
def editShortenLinks(slug):
    res = edit_url(request, slug)
    if not check_content_type(request.content_type):
        return Response(status=400)
    return res

if __name__ == '__main__':
   app.run(debug = True, port=5000)

