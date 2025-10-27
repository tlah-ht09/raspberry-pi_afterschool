import adafruit_dht
import board

sensor = adafruit_dht.DHT11(board.D18)

def get_now():
    temperature = sensor.temperature
    huminity = sensor.humidity
    return [temperature, huminity]
    
