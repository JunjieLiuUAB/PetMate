import os
os.environ["GPIOZERO_PIN_FACTORY"] = "lgpio"

from gpiozero import PhaseEnableMotor
from time import sleep

# Configuración de pines para DRI0002
M1_DIR = 17  
E1_PWM = 13  
M2_DIR = 22  
E2_PWM = 27  

motor_izquierdo = PhaseEnableMotor(phase=M1_DIR, enable=E1_PWM)
motor_derecho = PhaseEnableMotor(phase=M2_DIR, enable=E2_PWM)

def avanzar():
    motor_izquierdo.forward()
    motor_derecho.forward()

def retroceder():
    motor_izquierdo.backward()
    motor_derecho.backward()

def detener():
    motor_izquierdo.stop()
    motor_derecho.stop()

def girar_derecha():
    motor_izquierdo.forward()
    motor_derecho.backward()


print("Iniciando prueba de motores (Sentido corregido por Software)...")
print("Asegúrate de que las ruedas tengan espacio para girar libremente.\n")

try:
    while True:
        print("Avanzando...")
        avanzar()
        sleep(2.0)

        print("Deteniendo motores...")
        detener()
        sleep(1.0)
        
        print("Retrocediendo...")
        retroceder()
        sleep(2.0)

        print("Deteniendo motores...")
        detener()
        sleep(1.0)

except KeyboardInterrupt:
    detener()
    print("\nPrueba finalizada y motores detenidos.")

