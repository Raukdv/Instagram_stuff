from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView

class Template(TemplateView):
    template_name = 'template.html'

    def get_context_data(self, **kwargs):
        cliente_id='919424865298790'
        redirect_uri ='https://komando.aleoreina.com/'
        url = 'https://api.instagram.com/oauth/authorize?client_id='+cliente_id+'&redirect_uri='+redirect_uri+'&response_type=code'+'&scope=user_profile'
        context = super().get_context_data(**kwargs)
        context['link'] = url
        return context

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#from app.views import request
def request():
    import requests as r
    import json
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    data= {'client_id':'919424865298790',
            'client_secret':'dee2e7b9c920aa8d253cb27ffa659c72',
            'code':'AQCFQ02C1cDJ31fiQ_AYdvtWT7-v9_nIt2-UqrFq6dYPsp70OiUAxafJqtVB0K90k6X1XoSuB_mr6vxlPpN8niL1dA3Z_FetxVhBlclOfyXo4UWa5pt7x2bXZ18EdDWJU8EBkEsHsYRWZAnWE2BANVgWJQI4xN9-bTyyK84iq2rcME7rEPxWWaTT8Ww1ykubOltllNrv919tcaG3eW2bxbzSCK4l74NMdyT4Gbmjoh_EHA',
            'grant_type':'authorization_code',
            'redirect_uri':'https://komando.aleoreina.com/',
            }
    con = r.post('https://api.instagram.com/oauth/access_token',
                data=data,
                headers=headers,
                )

    data = json.loads(con.content.decode('utf-8'))
    at = data['access_token']
    ui= data['user_id']
    print('OBTENIENDO ID Y USERNAME')
    getting_user(at, ui)

def getting_user(acces_token, userid):
    import requests as r
    import json
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    con = r.get('https://graph.instagram.com/'+str(userid)+'?fields=id,username&access_token='+str(acces_token))
    data = json.loads(con.content.decode('utf-8'))

    print('ID DEL USUARIO: '+str(data['id']))
    print('NOMBRE DEL USUARIO: '+str(data['username']))