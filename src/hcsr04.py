from gpiozero import DistanceSensor

class HCSR04:
    """
    Drivers para Raspberry Pi 4 para los sonsores HC-SR04 
    """
    def __init__(self, trigger_pin, echo_pin):
        # gpiozero maneja internamente los tiempos de espera (timeouts)
        # gpiozero usa la numeración de pines BCM por defecto
        self._sensor = DistanceSensor(echo=echo_pin, trigger=trigger_pin, max_distance=4.0)

    def distance_cm(self):
        """
        devuelve la distancia en centímetros (float).
        """
        # gpiozero entrega la distancia en metros pero se pasa a cm
        return self._sensor.distance * 100
