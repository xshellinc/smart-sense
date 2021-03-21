def get_wbgt(temp, hum):
    return 0.725*temp + 0.0368*hum + 0.00364*hum*temp - 3.246


def get_wbgt_level(wbgt):
    if wbgt >= 31:
        return 4, "危険"
    if wbgt >= 28:
        return 3, "厳重警戒"
    if wbgt >= 25:
        return 2, "警戒"
    if wbgt >= 21:
        return 1, "注意"

    return 0, ""


if __name__ == '__main__':
    from sense_hat import SenseHat
    #from sense_emu import SenseHat
    #from dht22 import DHT22

    TEMP_DELTA = 0

    sense = SenseHat()
    #sense = DHT22()

    temp = sense.get_temperature() - TEMP_DELTA
    hum = sense.get_humidity()

    wbgt = get_wbgt(temp, hum)
    level, msg = get_wbgt_level(wbgt)

    print(f'Temperature: {temp}, Humidity: {hum}')
    print(f'WBGT: {wbgt}')
    print(f'Level: {level}, Message: {msg}')
