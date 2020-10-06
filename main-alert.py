from sense_hat import SenseHat
from ifttt import Webhook
from thi import *
from wbgt import *
from flu import *

import time


IFTTT_KEY = ''
CHECK_SPAN = 60 * 10

sense = SenseHat()
webhook = Webhook('demo', IFTTT_KEY)


def alert(message):
    payload = {
        "value1": message
    }
    res = webhook.post(event='send_message', payload=payload)
    print(res.ok)
    if not res.ok:
        print('Request failed with status code', res.status_code)

def main():
    thi_level = 0
    wbgt_level = 0
    vh_level = 0
    while True:
        temp = sense.get_temperature()
        hum = sense.get_humidity()

        payload = {
            "value1": temp,
            "value2": hum,
        }
        res = webhook.post(event='send_data', payload=payload)
        if not res.ok:
            print('Request failed with status code', res.status_code)

        thi = get_thi(temp, hum)
        level = get_thi_level(thi)
        if thi_level < 4 and level >= 4:
            alert('不快指数のレベルが上昇しています')

        wbgt = get_wbgt(temp, hum)
        level, msg = get_wbgt_level(wbgt)
        if wbgt_level < 4 and level >=4:
            alert(f'熱中症にご注意ください: {msg}')

        vh = get_vh(temp, hum)
        level, msg = get_flu_level(vh)
        if vh_level < 4 and level >=4:
            alert(f'インフルエンザにご注意ください: {msg}')

        time.sleep(CHECK_SPAN)


if __name__ == '__main__':
    main()
