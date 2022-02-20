from gpiozero import LED
from time import sleep

while True:
    red = LED(17) # Change 12 to your GPIO pin

    red.on()
    sleep(3)
    red.off()
