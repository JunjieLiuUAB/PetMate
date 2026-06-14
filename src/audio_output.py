import numpy as np
import sounddevice as sd

# --- CONFIGURACIÓN DEL AUDIO ---
SAMPLE_RATE = 48000      # Frecuencia de muestreo estándar
FRECUENCIA_TONO = 440.0  # Nota LA
DURACION = 2.0           # 2 segundos de pitido

print("Buscando amplificador I2S (MAX98357A)...")

# 1. Buscamos el ID del dispositivo de salida correcto de forma dinámica
devices = sd.query_devices()
id_dispositivo_salida = None

for i, device in enumerate(devices):
    # Buscamos las tarjetas asociadas al VoiceHat o al MAX98357A que tengan canales de salida
    if ("googlevoicehat" in device['name'].lower() or "max98357a" in device['name'].lower()) and device['max_output_channels'] > 0:
        id_dispositivo_salida = i
        print(f"-> ¡Amplificador encontrado! Dispositivo ID {i}: {device['name']}")
        break

if id_dispositivo_salida is None:
    print("⚠️ No se detectó el driver específico en Python. Intentando con el dispositivo por defecto...")

print("\nGenerando tono de prueba de 440Hz...")

try:
    # 2. Generamos la onda senoidal básica
    t = np.linspace(0, DURACION, int(SAMPLE_RATE * DURACION), False)
    onda_senoidal = np.sin(FRECUENCIA_TONO * t * 2 * np.pi)
    
    # 3. ¡CRÍTICO! Convertimos el audio a ESTÉREO (2 canales)
    # Duplicamos la onda para el canal izquierdo y el derecho
    audio_estereo = np.vstack((onda_senoidal, onda_senoidal)).T
    audio_data = (audio_estereo * 0.3).astype(np.float32)
    
    print("Reproduciendo por el altavoz...")
    
    # 4. Reproducimos forzando el uso de nuestro dispositivo I2S
    sd.play(audio_data, SAMPLE_RATE, device=id_dispositivo_salida)
    sd.wait()
    
    print("¡Prueba completada con éxito!")

except Exception as e:
    print(f"\nError al reproducir el audio: {e}")


"""
import numpy as np
import sounddevice as sd
from time import sleep

# --- CONFIGURACIÓN DEL AUDIO ---
SAMPLE_RATE = 44100  # Frecuencia de muestreo estándar (44.1kHz)
FRECUENCIA_TONO = 440.0  # Frecuencia de la nota LA (440Hz)
DURACION = 2.0  # Duración del pitido en segundos

print("Iniciando prueba del amplificador MAX98357A...")
print("Generando un tono de prueba de 440Hz por 2 segundos...")

try:
    # Generamos la onda senoidal (matemáticamente creamos el sonido)
    t = np.linspace(0, DURACION, int(SAMPLE_RATE * DURACION), False)
    onda_senoidal = np.sin(FRECUENCIA_TONO * t * 2 * np.pi)
    
    # Nos aseguramos de que el audio sea de tipo float32 y reducimos un poco el volumen (0.3)
    # para no saturar el altavoz pequeño en la primera prueba
    audio_data = (onda_senoidal * 0.3).astype(np.float32)
    
    # Reproducimos el sonido
    sd.play(audio_data, SAMPLE_RATE)
    
    # Esperamos a que termine de reproducir
    sd.wait()
    
    print("¡Prueba completada con éxito!")

except Exception as e:
    print(f"\nError al reproducir el audio: {e}")
    print("Verifica que añadiste 'dtoverlay=max98357a' en config.txt y reiniciaste la Pi.")
    """