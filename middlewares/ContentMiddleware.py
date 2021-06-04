from werkzeug.wrappers import Request, Response, ResponseStream

class ContentMiddleware():
    def __init__(self, app):
        self.app = app

    def __check_content_type(self, reqContent):
        if(reqContent and reqContent.startswith('application/json')):
            return True
        return False

    def __call__(self, environ, start_response):
        req = Request(environ)
        print(req)
        if not self.__check_content_type(req.content_type):
            res = Response(status=401)
            return res(environ, start_response)
        else:
            return self.app(environ, start_response)
