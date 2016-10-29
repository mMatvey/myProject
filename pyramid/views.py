from pyramid.response import Response
from pyramid.view import view_config

@view_config(renderer="index.html")
def hello_view(request):
    return Response("""<a href="index.html">asd</a> <br> <a href="http://localhost:8000/index.html">zxc</a>""")

@view_config(renderer="about.html")
def hello_view(request):
    return Response("""<a href="about/aboutme.html">asd</a> <br> <a href="http://localhost:8000/about/aboutme.html">zxc</a>""")
