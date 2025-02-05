def get_vh(temp, hum):
    return 217*(6.1078*10**(7.5*temp/(temp+237.3)))/(temp+273.15)*hum/100


def get_flu_level(vh):
    if vh > 17:
        return 1, "非常に安全"
    if vh > 11:
        return 2, "安全"
    if vh > 7:
        return 3, "要注意"

    return 4, "警戒"


if __name__ == '__main__':
    from sense_hat import SenseHat as Sensor
    #from sense_emu import SenseHat as Sensor
    #from dht22 import DHT22 as Sensor

    TEMP_DELTA = 0

    sense = Sensor()

    temp = sense.get_temperature() - TEMP_DELTA
    hum = sense.get_humidity()

    vh = get_vh(temp, hum)
    level, msg = get_flu_level(vh)

    print(f'Temperature: {temp}, Humidity: {hum}')
    print(f'Volumetric humidity: {vh}')
    print(f'Level: {level}, Message: {msg}')
