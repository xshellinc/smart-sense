from ifttt import Webhook

IFTTT_KEY = '{IFTTT-KEY-HERE}'

webhook = Webhook('send_data', IFTTT_KEY)

payload = {
    "value1": "test1",          
    "value2": "test2",
    "value3": "test3",
}

res = webhook.post(payload=payload)
print("send")
if not res.ok:
    print('Request failed with status code', res.status_code)
