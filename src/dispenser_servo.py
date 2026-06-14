
import os
os.environ["GPIOZERO_PIN_FACTORY"] = "lgpio"

from gpiozero import Servo
from time import sleep

MIN_PULSE = 0.5 / 1000
MAX_PULSE = 2.5 / 1000

servo = Servo(4, min_pulse_width=MIN_PULSE, max_pulse_width=MAX_PULSE)

print("Iniciando control del servo MG90S...")

try:
    while True:
        print("Ángulo: 90°")
        servo.max()
        sleep(1.5)

        
        print("Ángulo: 45°")
        servo.value = -0.70
        sleep(1.5)

        
        #print("Ángulo: 180°")
        #servo.max()
        #sleep(1.5)
        

except KeyboardInterrupt:
    servo.value = None
    print("\nPrograma detenido.")