import web_api
from django.shortcuts import render, render_to_response
from django.utils import simplejson


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    #if not request.POST:
    #    return render_to_response('dashboard.html', {})
    results_list = {}
    api = web_api.api
    results_list.update(api.get_stats())
    return render_to_response('dashboard.html', results_list)