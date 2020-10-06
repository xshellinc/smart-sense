import requests


class Webhook:
    def __init__(self, event_name, ifttt_key):
        self.event_name = event_name
        self.ifttt_key = ifttt_key
        self.update_url()

    def update_url(self, event=None):
        if event:
            self.event_name = event
        self.url = "https://maker.ifttt.com/trigger/" + \
            self.event_name + "/with/key/" + self.ifttt_key

    def post(self, *, event=None, payload={}):
        if event:
            self.update_url(event)
        response = requests.post(self.url, data=payload)
        return response
