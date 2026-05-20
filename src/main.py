import sensores
import time

# inicilizar una sola vez al arrancar
sensores.inicializar_pines()

# usar en bucle
distancia = sensores.leer_ultrasonico_frontal()
print(f"El obstáculo está a {distancia} cm")

#  limpias los pines al cerrar
# sensores.limpiar_gpio()
