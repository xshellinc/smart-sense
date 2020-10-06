def get_wbgt(temp, hum):
    return 0.725*temp + 0.0368*hum + 0.00364*hum*temp - 3.246


def get_wbgt_level(wbgt):
    if wbgt < 25:
        return 1, "注意"
    if wbgt < 28:
        return 2, "警戒"
    if wbgt < 31:
        return 3, "厳重警戒"
    else:
        return 4, "危険"


if __name__ == '__main__':
    from sense_hat import SenseHat

    sense = SenseHat()

    temp = sense.get_temperature()
    hum = sense.get_humidity()

    wbgt = get_wbgt(temp, hum)
    level, msg = get_wbgt_level(wbgt)

    print(f'WBGT: {wbgt}')
    print(f'Level: {level}, Message: {msg}')
