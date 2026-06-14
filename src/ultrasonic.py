import time
from gpiozero import DistanceSensor

class HCSR04:
    """
    Drivers para Raspberry Pi 4 para los sonsores HC-SR04 
    """
    def __init__(self, trigger_pin, echo_pin):
        # gpiozero maneja internamente los tiempos de espera y usa la numeración de pines BCM por defecto
        self._sensor = DistanceSensor(echo=echo_pin, trigger=trigger_pin, max_distance=4.0)

    def distance_cm(self):
        """
        devuelve la distancia en centímetros (float).
        """
        # gpiozero entrega la distancia en metros pero se pasa a cm
        return self._sensor.distance * 100



if __name__ == "__main__":
    print("Iniciando los 3 sensores ultrasónicos...")
    #29
    sensor_cen = HCSR04(trigger_pin=5, echo_pin=6)
    #36
    #sensor_izq = HCSR04(trigger_pin=26, echo_pin=12)
    #16
    #sensor_der = HCSR04(trigger_pin=23, echo_pin=24)

    #izquierod y derecho al reves estan asi que:
    sensor_der = HCSR04(trigger_pin=26, echo_pin=12)
    
    sensor_izq = HCSR04(trigger_pin=23, echo_pin=24)

    
    try:
        while True:
            d_izq = sensor_izq.distance_cm()
            d_cen = sensor_cen.distance_cm()
            d_der = sensor_der.distance_cm()
            
            print(f"Izquierda: {d_izq:.1f} cm | Centro: {d_cen:.1f} cm | Derecha: {d_der:.1f} cm")
            #print(f"Centro: {d_cen:.1f} cm | Derecha: {d_der:.1f} cm")
            #print(f"Derecha: {d_der:.1f} cm")
            #print(f"Centro: {d_cen:.1f} cm")
            
            # Pausa  
            time.sleep(0.2)
            
    except KeyboardInterrupt:
        print("\nPrograma detenido por el usuario.")
