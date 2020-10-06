def get_thi(temp, hum):
    return 0.81*temp + 0.01*hum*(0.99*temp-14.3) + 46.3


def get_thi_level(thi):
    if thi < 70:
        return 1
    elif thi < 75:
        return 2
    elif thi < 80:
        return 3
    elif thi < 85:
        return 4
    else:
        return 5


if __name__ == '__main__':
    from sense_hat import SenseHat

    sense = SenseHat()

    temp = sense.get_temperature()
    hum = sense.get_humidity()

    thi = get_thi(temp, hum)
    level = get_thi_level(thi)

    print(f'TH-index: {thi}, TH-level: {level}')
