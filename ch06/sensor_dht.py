import adafruit_dht
import board

def get_now():
    sensor = adafruit_dht.DHT11(board.D18)
    temperature = sensor.temperature
    huminity = sensor.humidity
    return [temperature, huminity]