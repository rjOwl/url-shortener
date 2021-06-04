from werkzeug.wrappers import Request, Response, ResponseStream
from flask_cors import CORS, cross_origin

class ContentMiddleware():
    def __init__(self, app):
        self.app = app

    def __check_content_type(self, reqContent):
        if(reqContent and reqContent.startswith('application/json')):
            return True
        return False

    def __call__(self, environ, start_response):
        start_response.headers.add("Access-Control-Allow-Origin", "*")
        req = Request(environ)
        if not self.__check_content_type(req.content_type):
            res = Response(u'Non-JSON Content-Type', mimetype= 'text/plain', status=400)
            return res(environ, start_response)
        else:
            return self.app(environ, start_response)
