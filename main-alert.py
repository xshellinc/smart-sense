from sense_hat import SenseHat
#from sense_emu import SenseHat
from ifttt import Webhook
from wbgt import *
from flu import *

import time
from datetime import datetime


IFTTT_KEY = ''
TEMP_DELTA = 0
CHECK_SPAN = 60 * 10

sense = SenseHat()
# イベント名は後で変更するので最初は何でも良い
webhook = Webhook('demo', IFTTT_KEY)


def alert(message):
    payload = {
        "value1": message
    }
    res = webhook.post(event='send_message', payload=payload)
    if not res.ok:
        print('Request failed with status code', res.status_code)


def main():
    wbgt_level = 0
    vh_level = 0
    while True:
        now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        temp = sense.get_temperature() - TEMP_DELTA
        hum = sense.get_humidity()

        payload = {
            "value1": now,
            "value2": temp,
            "value3": hum,
        }
        res = webhook.post(event='send_data', payload=payload)
        if not res.ok:
            print('Request failed with status code', res.status_code)

        '''
        熱中症警戒度が3以上に変化したらアラートを出す
        '''
        wbgt = get_wbgt(temp, hum)
        level, msg = get_wbgt_level(wbgt)
        if (wbgt_level < 3 and level >= 3) or (wbgt_level < 4 and level >= 4):
            alert(f'【{msg}】熱中症にご注意ください！現在の暑さ指数は{round(wbgt)}です。')
        wbgt_level = level

        '''
        インフルエンザ警戒度が3以上に変化したらアラートを出す
        '''
        vh = get_vh(temp, hum)
        level, msg = get_flu_level(vh)
        if (vh_level < 3 and level >= 3) or (vh_level < 4 and level >= 4):
            alert(f'【{msg}】インフルエンザにご注意ください。現在の絶対湿度は{round(vh)}g/m3です。加湿しましょう。')
        vh_level = level

        time.sleep(CHECK_SPAN)


if __name__ == '__main__':
    main()
