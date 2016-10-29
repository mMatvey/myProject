from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def index(request):
    return Response("""<a href="index.html">asd</a> <br> <a href="http://localhost:8000/index.html">zxc</a>""")
def about(request):
    return Response("""<a href="about/aboutme.html">asd1</a> <br> <a href="http://localhost:8000/about/aboutme.html">zxc1</a>""")

if __name__ == '__main__':
    config = Configurator()
    config.add_route('index', '/')
    config.add_view(index, route_name='index')
    config.add_route('about', 'about')
    config.add_view(about, route_name='about')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
