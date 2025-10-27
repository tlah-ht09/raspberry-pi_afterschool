import adafruit_dht
import board

sensor = adafruit_dht.DHT11(board.D14)

def get_now():

    temperature = sensor.temperature
    huminity = sensor.humidity
    return [temperature, huminity]
    


