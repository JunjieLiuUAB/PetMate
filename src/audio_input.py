#SE NECESITA ENTORNO VIRUAL VENV

import numpy as np
import sounddevice as sd
from time import sleep

# config audio
SAMPLE_RATE = 48000  
CHANNELS = 2         
DURACION_BLOQUE = 0.1 

print("Iniciando prueba del micrófono digital SPH0645 (I2S)...")
print("Habla o haz ruido cerca del micrófono.\n")
print("Presiona Ctrl+C para salir.\n")

# seleccion dispositivo
devices = sd.query_devices()
for i, device in enumerate(devices):
    if "googlevoicehat" in device['name'].lower() and device['max_input_channels'] > 0:
        sd.default.device = i
        print(f"-> Usando dispositivo de entrada: {device['name']} (ID: {i})")
        break

try:
    # flujo entrada audio
    with sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS) as stream:
        while True:
            data, overflow = stream.read(int(SAMPLE_RATE * DURACION_BLOQUE))
            rms = np.sqrt(np.mean(data[:, 0]**2)) if data.ndim > 1 else np.sqrt(np.mean(data**2))
            
            # normalizar valor
            intensidad = min(rms * 10, 1.0)
            
            #  barra visual para la terminal
            num_barras = int(intensidad * 50)
            barra_visual = "█" * num_barras
            
            # mostrar el volumen 
            print(f"Volumen: {rms:.4f} | {barra_visual:<50}", end="\r")

except KeyboardInterrupt:
    print("\n\nPrueba finalizada.")
except Exception as e:
    print(f"\nError: {e}")
    print("Asegúrate de haber configurado el archivo /boot/firmware/config.txt y reiniciado la Pi.")

