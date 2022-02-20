import RPi.GPIO as GPIO
import time
from urllib.request import urlopen
from gpiozero import LED


__author__ = 'Gus (Adapted from Adafruit)'
__license__ = "GPL"
__maintainer__ = "pimylifeup.com"

#GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pin_to_circuit = 16

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count




GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
red = LED(17)
PIR_PIN = 22
GPIO.setup(PIR_PIN, GPIO.IN)
myAPI="V4MZ9K5GVTMSDUGN"
baseURL ="https://api.thingspeak.com/update?api_key=V4MZ9K5GVTMSDUGN&field1=0"
url = baseURL.replace(" ","")
print('Starting up the PIR Module (click on STOP to exit)')
time.sleep(1)
print ('Ready')

while True:
  
  motion = GPIO.input(PIR_PIN)
  light= rc_time(pin_to_circuit)/100
  conn=urlopen(url+'&field1=%s&field2=%s'%(motion,light))
  print(rc_time(pin_to_circuit)/100)
  seuil = 291
  if GPIO.input(PIR_PIN) and light < seuil:
      print('Motion Detected')
      print('light == 0')
      red.on()
  else:
    print('No Motion Detected') 
    red.off()
      
     
    
  time.sleep(1)