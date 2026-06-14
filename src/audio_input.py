
#SE NECESITA ENTORNO VIRUAL VENV

import numpy as np
import sounddevice as sd
from time import sleep

# --- CONFIGURACIÓN DEL AUDIO ---
# El SPH0645 funciona de forma óptima a estas frecuencias
SAMPLE_RATE = 48000  # Frecuencia de muestreo 
CHANNELS = 2         # Stereo
DURACION_BLOQUE = 0.1 # Tiempo en segundos de cada lectura (100ms)

print("Iniciando prueba del micrófono digital SPH0645 (I2S)...")
print("Habla o haz ruido cerca del micrófono.\n")
print("Presiona Ctrl+C para salir.\n")

# --- FORZAR SELECCIÓN DE DISPOSITIVO ---
devices = sd.query_devices()
for i, device in enumerate(devices):
    if "googlevoicehat" in device['name'].lower() and device['max_input_channels'] > 0:
        sd.default.device = i
        print(f"-> Usando dispositivo de entrada: {device['name']} (ID: {i})")
        break

try:
    # Creamos un flujo de entrada de audio (InputStream)
    with sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS) as stream:
        while True:
            # Leemos un bloque de datos de audio
            # 'data' es una matriz de números flotantes entre -1.0 y 1.0
            data, overflow = stream.read(int(SAMPLE_RATE * DURACION_BLOQUE))
            
            # Calculamos la energía del sonido usando RMS (Root Mean Square)
            # Esto nos da la intensidad real del volumen
            #rms = np.sqrt(np.mean(data**2))
            #Cambio anterior por:
            rms = np.sqrt(np.mean(data[:, 0]**2)) if data.ndim > 1 else np.sqrt(np.mean(data**2))
            
            # Normalizamos el valor para que sea más fácil de ver en la barra (multiplicamos por 10)
            intensidad = min(rms * 10, 1.0)
            
            # Creamos la barra visual para la terminal
            num_barras = int(intensidad * 50)
            barra_visual = "█" * num_barras
            
            # Mostramos el volumen en tiempo real
            print(f"Volumen: {rms:.4f} | {barra_visual:<50}", end="\r")

except KeyboardInterrupt:
    print("\n\nPrueba finalizada.")
except Exception as e:
    print(f"\nError: {e}")
    print("Asegúrate de haber configurado el archivo /boot/firmware/config.txt y reiniciado la Pi.")


"""
import os
os.environ["GPIOZERO_PIN_FACTORY"] = "lgpio"

from gpiozero import MCP3008
from time import sleep

# Configuramos el MCP3008 en el canal 0 (donde está el micrófono)
# gpiozero maneja las conexiones SPI por defecto en los pines nativos
mic = MCP3008(channel=0)

print("Iniciando prueba del micrófono electret...")
print("Habla o haz ruido cerca del micrófono para ver los cambios.\n")

try:
    while True:
        # mic.value devuelve un número flotante entre 0.0 y 1.0
        lectura = mic.value
        
        # Creamos una barra visual en la terminal según la intensidad
        num_barras = int(lectura * 50)
        barra_visual = "█" * num_barras
        
        # Mostramos el valor numérico y la barra
        print(f"Intensidad: {lectura:.4f} | {barra_visual:<50}", end="\r")
        
        # Pequeña pausa para no saturar la CPU
        sleep(0.05)

except KeyboardInterrupt:
    print("\n\nPrueba finalizada.")

"""