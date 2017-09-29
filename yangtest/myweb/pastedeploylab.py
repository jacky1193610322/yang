import os
from webob import Request
from webob import Response
from paste.deploy import loadapp
from wsgiref.simple_server import make_server
from webob.dec import wsgify


class LogFilter(object):
    def __init__(self,app):
        self.application = app
        pass

    @wsgify()
    def __call__(self, req):
        print("filter:LogFilter is called.")
        res = req.get_response(self.application)
        print("begin  aaaaaaaaaa")
        print(res)
        print("end aaaaaaaaaa")
        return res

    @classmethod
    def factory(cls, global_conf, **kwargs):
        print("cls", cls)
        print("in LogFilter.factory", global_conf, kwargs)
        return LogFilter


class LogFilter1(object):
    def __init__(self, app):
        self.application = app
        pass

    @wsgify()
    def __call__(self, req):
        print("filter:LogFilterbeifen is called.")
        res = req.get_response(self.application)
        print("begin  bbbbbbbbbbb")
        print(res)
        res.body += "chenyang"
        print(res)
        print("end bbbbbbbbbbb")
        return res

    @classmethod
    def factory(cls, global_conf, **kwargs):
        print("cls", cls)
        print("in LogFilterbeifen1.factory", global_conf, kwargs)
        return LogFilter1


class ShowVersion(object):
    def __init__(self):
        pass

    @wsgify()
    def __call__(self, req):
        app = ShowVersion2()
        return app

    @classmethod
    def factory(cls, global_conf, **kwargs):
        print "in ShowVersion.factory", global_conf, kwargs
        return ShowVersion()


class ShowVersion2(object):
    def __init__(self):
        pass

    def __call__(self, environ, start_response):
        start_response("200 OK", [("Content-type", "text/plain")])

        return ["version 2", ]

    @classmethod
    def factory(cls, global_conf, **kwargs):
        print "in ShowVersion222222.factory", global_conf, kwargs
        return ShowVersion2()


class Calculator(object):
    def __init__(self):
        pass

    def __call__(self, environ, start_response):
        req = Request(environ)
        res = Response()
        res.status = "200 OK"
        res.content_type = "text/plain"
        # get operands
        operator = req.GET.get("operator", None)
        operand1 = req.GET.get("operand1", None)
        operand2 = req.GET.get("operand2", None)
        print req.GET
        opnd1 = int(operand1)
        opnd2 = int(operand2)
        if operator == u'plus':
            opnd1 = opnd1 + opnd2
        elif operator == u'minus':
            opnd1 = opnd1 - opnd2
        elif operator == u'star':
            opnd1 = opnd1 * opnd2
        elif operator == u'slash':
            opnd1 = opnd1 / opnd2
        res.body = "%s /nRESULT= %d" % (str(req.GET) , opnd1)
        return res(environ, start_response)

    @classmethod
    def factory(cls, global_conf, **kwargs):
        print "in Calculator.factory", global_conf, kwargs
        return Calculator()


if __name__ == '__main__':
    configfile = "pastedeploylab.ini"
    appname = "pdl"
    wsgi_app = loadapp("config:%s" % os.path.abspath(configfile), appname)
    server = make_server('localhost', 8081, wsgi_app)
    server.serve_forever()
