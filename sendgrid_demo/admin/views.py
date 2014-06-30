import json
import web_api
from django.shortcuts import render, render_to_response


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    #if not request.POST:
    #    return render_to_response('dashboard.html', {})
    user = 'stimko68'
    api_key = '6gpk2PXv5GyD'

    api = web_api.WebAPI(user, api_key)
    results_list = json.loads(api.get_stats())
    """results_list = [{
        'delivered': 0,
        'unsubscribes': 0,
        'opens': 0,
        'invalid_email': 0,
        'bounces': 0,
        'repeat_unsubscribes': 0,
        'unique_opens': 0,
        'spam_drop': 0,
        'repeat_bounces': 0,
        'repeat_spamreports': 0,
        'date': '2014-06-29',
        'requests': 0,
        'spamreports': 0,
        'clicks': 0,
        'unique_clicks': 0,
        'blocked': 0
    }, {
        'delivered': 1200,
        'unsubscribes': 0,
        'opens': 20,
        'invalid_email': 10,
        'bounces': 0,
        'repeat_unsubscribes': 0,
        'unique_opens': 20,
        'spam_drop': 0,
        'repeat_bounces': 0,
        'repeat_spamreports': 0,
        'date': '2014-06-28',
        'requests': 0,
        'spamreports': 10,
        'clicks': 200,
        'unique_clicks': 200,
        'blocked': 0
    }]"""

    return render(request, 'dashboard.html', results_list[0])