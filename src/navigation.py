
import os
import time

os.environ["GPIOZERO_PIN_FACTORY"] = "lgpio"
from gpiozero import PhaseEnableMotor, DistanceSensor

# ULTRASONIDOS 
class HCSR04:
    def __init__(self, trigger_pin, echo_pin):
        self._sensor = DistanceSensor(echo=echo_pin, trigger=trigger_pin, max_distance=4.0)

    def distance_cm(self):
        return self._sensor.distance * 100

# controlador DRI0002
M1_DIR = 17  
E1_PWM = 13  
M2_DIR = 22  
E2_PWM = 27  

motor_izquierdo = PhaseEnableMotor(phase=M1_DIR, enable=E1_PWM)
motor_derecho = PhaseEnableMotor(phase=M2_DIR, enable=E2_PWM)

# Funciones movimiento

def avanzar(velocidad=1.0):
    motor_izquierdo.forward(velocidad)
    motor_derecho.forward(velocidad)

def girar_izquierda(velocidad=1.0):
    motor_izquierdo.backward(velocidad)
    motor_derecho.forward(velocidad)

def detener():
    motor_izquierdo.stop()
    motor_derecho.stop()

def fijar_velocidades(vel_izq, vel_der):
    if vel_izq >= 0:
        motor_izquierdo.forward(vel_izq)
    else:
        motor_izquierdo.backward(abs(vel_izq))
        
    if vel_der >= 0:
        motor_derecho.forward(vel_der)
    else:
        motor_derecho.backward(abs(vel_der))


# Configuración de Sensores (Centro, Derecha e Izquierda)
print("Inicializando sensores...")
sensor_cen = HCSR04(trigger_pin=5, echo_pin=6)
sensor_der = HCSR04(trigger_pin=26, echo_pin=12) 
sensor_izq = HCSR04(trigger_pin=23, echo_pin=24)

# parametros
VEL_BASE = 0.9          # Velocidad general 
DIST_FRENTE_MIN = 35.0   # cm. Si hay algo más cerca al frente, frena y gira
DIST_PARED_MIN = 12.0    # cm. Distancia mínima a la pared derecha para no rozar
DIST_PARED_MAX = 40.0    # cm. Si la pared está más lejos, gírate para buscarla

print("\n¡Comenzando Wall-Following con DRI0002 (Pared a la derecha)!")
print("Presiona Ctrl+C para detener el robot.\n")

# Damos un segundo para soltar el robot antes de que empiece a moverse
time.sleep(1)

try:
    while True:
        # Leer distancias
        d_cen = sensor_cen.distance_cm()
        d_der = sensor_der.distance_cm()
        d_izq = sensor_izq.distance_cm()
        
        # 1. Obstáculo al frente
        if d_cen < DIST_FRENTE_MIN:
            print(f"Obstáculo al frente ({d_cen:.1f} cm) -> Girando a la IZQUIERDA")
            girar_izquierda(VEL_BASE/2.3)

        # 2. Obstáculo a la izquierda
        elif d_izq < DIST_PARED_MIN:
            print(f"Peligro a la izquierda ({d_izq:.1f} cm) -> Ajustando DERECHA")
            fijar_velocidades(VEL_BASE, 0.5) #antes 0.35 

        # 3. Seguimiento pared derecha
        else:
            if d_der < DIST_PARED_MIN:
                # Muy cerca: curva suave a la izquierda para separarnos
                print(f"Muy cerca de la pared ({d_der:.1f} cm) -> Ajustando IZQUIERDA")
                # Rueda derecha más rápida que la izquierda
                fijar_velocidades(0.5, VEL_BASE) 

            elif d_der > DIST_PARED_MAX:
                # Muy lejos (o hueco/esquina): curva hacia la derecha para buscar pared
                print(f"Buscando pared ({d_der:.1f} cm) -> Ajustando DERECHA")
                # Rueda izquierda más rápida que la derecha
                fijar_velocidades(VEL_BASE, 0.5) 

            else:
                # Distancia perfecta (entre MIN y MAX): ir recto
                print(f"Trayectoria correcta (Izquierda: {d_izq:.1f} cm, Centro: {d_cen:.1f} cm, Der: {d_der:.1f} cm) -> RECTO")
                avanzar(VEL_BASE)
                
        # Pequeña pausa para dar tiempo a los motores y sensores a actualizarse
        time.sleep(0.1)

except KeyboardInterrupt:
    # Parada de emergencia y apagado limpio
    detener()
    print("\nPrograma detenido. Motores apagados.")

