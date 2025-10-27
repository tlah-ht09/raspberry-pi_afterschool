import adafruit_dht
import board

sensor = adafruit_dht.DHT11(board.D18)

def get_now():
    try:
        temperature = sensor.temperature
        huminity = sensor.humidity
        return [temperature, huminity]
    
    except : 
        print("실패")
        return ['실','패']

