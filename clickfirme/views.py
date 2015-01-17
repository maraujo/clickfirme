from pyramid.view import view_config
from cornice import Service
import json
import os

api_service = Service(name='api', path='/api', description="ZeLoteria API")

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'clickfirme'}

def is_loteria(request):
    if not "loteria" in request.GET:
        request.errors.add("query","loteria","Precisa do parametro loteria")
    elif request.GET["loteria"] != "megasena":
        request.errors.add("query","loteria","Precisa do parametro loteria=megasena")

@api_service.get(validators=is_loteria)
def get_loteria(request):
    file_ptr = open(os.path.abspath(os.path.dirname(__file__)) + "/crawlers/raffle/megasena.json","r")
    content = file_ptr.read()
    file_ptr.close()

    return json.loads(content)

