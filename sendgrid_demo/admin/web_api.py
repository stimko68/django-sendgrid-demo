"""
Program that handles the Web API calls
"""
import argparse
import json
import sendgrid
import urllib

#Authentication Credentials
USERNAME = 'stimko68'
PASSWORD = '6gpk2PXv5GyD'


class WebAPI(object):

    def __init__(self, user, api_key):
        self.user = user
        self.api_key = api_key
        self.base_url = 'https://api.sendgrid.com/api/'

    def get_stats(self, days=None, start_date=None, end_date=None, aggregate=None, category=None):
        option = 'stats.get.json'
        auth = "?api_user={}&api_key={}".format(self.user, self.api_key)
        options = {
            'days': days,
            'start_date': start_date,
            'end_date': end_date,
            'aggregate': aggregate,
            'category': category,
        }
        extras = ''
        for key, value in options.items():
            if value is not None:
                extras += "&{}={}".format(key, value)
        response = urllib.urlopen(self.base_url+option+auth+extras)
        return response.read()

    def send_email(self, recipients, sender, subject, message_body):
        sg = sendgrid.SendGridClient(self.user, self.api_key)
        message = sendgrid.Mail(to=recipients, from_email=sender, subject=subject, text=message_body)
        return sg.send(message)

    def view_blocks(self, date=None, days=None, start_date=None, end_date=None, limit=None, offset=None):
        option = 'blocks.get.json'
        auth = "?api_user={}&api_key={}".format(self.user, self.api_key)
        options = {
            'date': date,
            'days': days,
            'start_date': start_date,
            'end_date': end_date,
            'limit': limit,
            'offset': offset,
        }
        extras = ''
        for key, value in options.items():
            if value is not None:
                extras += "&{}={}".format(key, value)
        response = urllib.urlopen(self.base_url+option+auth+extras)
        return response.read()

    def view_bounces(self, date=None, days=None, start_date=None, end_date=None, limit=None,
                     offset=None, bounce_type=None, email=None):
        option = 'bounces.get.json'
        auth = "?api_user={}&api_key={}".format(self.user, self.api_key)
        options = {
            'date': date,
            'days': days,
            'start_date': start_date,
            'end_date': end_date,
            'limit': limit,
            'offset': offset,
            'type': bounce_type,
            'email': email,
        }
        extras = ''
        for key, value in options.items():
            if value is not None:
                extras += "&{}={}".format(key, value)
        response = urllib.urlopen(self.base_url+option+auth+extras)
        return response.read()


if __name__ == "__main__":
    api = WebAPI(USERNAME, PASSWORD)
    result = json.loads(api.get_stats())

    for item in result:
        print item