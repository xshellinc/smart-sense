def get_thi(temp, hum):
    return 0.81*temp + 0.01*hum*(0.99*temp-14.3) + 46.3


def get_thi_level(thi):
    if thi < 70:
        return 1
    if thi < 75:
        return 2
    if thi < 80:
        return 3
    if thi < 85:
        return 4

    return 5


if __name__ == '__main__':
    from sense_hat import SenseHat
    #from sense_emu import SenseHat
    #from dht22 import DHT22

    TEMP_DELTA = 0

    sense = SenseHat()
    #sense = DHT22()

    temp = sense.get_temperature() - TEMP_DELTA
    hum = sense.get_humidity()

    thi = get_thi(temp, hum)
    level = get_thi_level(thi)

    print(f'Temperature: {temp}, Humidity: {hum}')
    print(f'TH-index: {thi}')
    print(f'Level: {level}')
