import os
os.environ["GPIOZERO_PIN_FACTORY"] = "lgpio"

from gpiozero import PhaseEnableMotor
from time import sleep

# Configuración de pines para DRI0002
M1_DIR = 17  
E1_PWM = 13  
M2_DIR = 22  
E2_PWM = 27  

# Creamos los motores de forma limpia (sin argumentos que den error)
motor_izquierdo = PhaseEnableMotor(phase=M1_DIR, enable=E1_PWM)
motor_derecho = PhaseEnableMotor(phase=M2_DIR, enable=E2_PWM)

# --- INVERSIÓN MANUAL DE SENTIDO ---
# Como los motores giraban al revés, hacemos que la función "avanzar"
# mande la señal de retroceso a los motores, y viceversa.

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
    # Ajusta esto según cómo responda el robot al girar
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


"""
import os
os.environ["GPIOZERO_PIN_FACTORY"] = "lgpio"

# Importamos directamente PhaseEnableMotor en lugar del Robot completo
from gpiozero import PhaseEnableMotor
from time import sleep

# Configuración de pines para DRI0002
M1_DIR = 17  
E1_PWM = 13  
M2_DIR = 22  
E2_PWM = 27  

# Creamos los motores de forma independiente
motor_izquierdo = PhaseEnableMotor(phase=M1_DIR, enable=E1_PWM)
motor_derecho = PhaseEnableMotor(phase=M2_DIR, enable=E2_PWM)

# Funciones manuales para replicar el comportamiento de 'Robot'
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


print("Iniciando prueba de motores con controlador DRI0002 (Fix Manual)...")
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
        
    
        print("Girando a la derecha...")
        girar_derecha()
        sleep(1.5)

        print("Deteniendo motores...")
        detener()
        sleep(2.0)
        

except KeyboardInterrupt:
    detener()
    print("\nPrueba finalizada y motores detenidos.")
"""
"""
import os
os.environ["GPIOZERO_PIN_FACTORY"] = "lgpio"

from gpiozero import Robot
from time import sleep

# Formato: Robot(izquierdo=(IN1, IN2), derecho=(IN3, IN4))
#robot = Robot(left=(13, 22), right=(27, 17))
#robot = Robot(left=(13, 17), right=(27, 22))
robot = Robot(left=(17, 13), right=(22, 27))

print("Iniciando prueba de motores...")
print("Asegúrate de que las ruedas tengan espacio para girar libremente.\n")

try:
    while True:
        print("Avanzando...")
        robot.forward()
        sleep(2.0)

        print("Deteniendo motores...")
        robot.stop()
        sleep(1.0)
        
        print("Retrocediendo...")
        robot.backward()
        sleep(2.0)

        print("Deteniendo motores...")
        robot.stop()
        sleep(1.0)
        
        print("Avanzando...")
        robot.forward()
        sleep(2.0)

        print("Deteniendo motores...")
        robot.stop()
        sleep(1.0)

        print("Girando a la derecha...")
        robot.right()
        sleep(1.5)

        print("Deteniendo motores...")
        robot.stop()
        sleep(2.0)
        

except KeyboardInterrupt:
    robot.stop()
    print("\nPrueba finalizada y motores detenidos.")

"""