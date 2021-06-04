from flask import Flask, helpers, redirect, url_for, request, json, jsonify, Response
from werkzeug.wrappers import response
from controllers.UrlController import *
import boot.DBConnection
from middlewares.ContentMiddleware import ContentMiddleware

app = Flask(__name__)
app.wsgi_app = ContentMiddleware(app.wsgi_app)

# Return all shortend links with slug
@app.route('/shortlinks',methods = ['GET'])
def getShortendLinks():
    return get_urls(request)

    # data = {
    #     "link": "asd",
    #     "ASD":123
    # }
    # if not check_content_type(request.content_type):
    #     return "Non-JSON Content-Type", 400
    # return data, 200



@app.route('/shortlinks', methods = ['POST'])
def shortenLink():
    return create_short_url(request)


# Get the slug and edit the link
@app.route('/shortlinks/<slug>',methods = ['PUT'])
def editShortenLinks(slug):
    res = edit_url(request, slug)
    print(request)
    # print(slug)
    return res
    # return jsonify(slug)

if __name__ == '__main__':
   app.run(debug = True)


