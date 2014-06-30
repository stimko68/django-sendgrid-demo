import json
import web_api
from django.shortcuts import render, render_to_response, HttpResponse

user = 'stimko68'
api_key = '6gpk2PXv5GyD'


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    #if not request.POST:
    #    return render_to_response('dashboard.html', {})

    api = web_api.WebAPI(user, api_key)
    results_list = json.loads(api.get_stats())

    return render(request, 'dashboard.html', results_list[0])
    #return HttpResponse(json.dumps(results_list, cls=DjangoJSONEncoder), content_type='application/json')


def send_email(request):
    if not request.POST:
        return render_to_response('send_email.html', {})

    api = web_api.WebAPI(user, api_key)
    email_result = json.dumps(api.send_email())
    return render_to_response('send_email.html', email_result)