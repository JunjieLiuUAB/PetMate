import numpy as np
import sounddevice as sd

# config audio
SAMPLE_RATE = 48000      
FRECUENCIA_TONO = 440.0  
DURACION = 2.0           

print("Buscando amplificador I2S (MAX98357A)...")

# buscar ID del dispositivo 
devices = sd.query_devices()
id_dispositivo_salida = None

for i, device in enumerate(devices):
    # buscar tarjetas asociadas 
    if ("googlevoicehat" in device['name'].lower() or "max98357a" in device['name'].lower()) and device['max_output_channels'] > 0:
        id_dispositivo_salida = i
        print(f"-> ¡Amplificador encontrado! Dispositivo ID {i}: {device['name']}")
        break

if id_dispositivo_salida is None:
    print("⚠️ No se detectó el driver específico en Python. Intentando con el dispositivo por defecto...")

print("\nGenerando tono de prueba de 440Hz...")

try:
    # generar onda
    t = np.linspace(0, DURACION, int(SAMPLE_RATE * DURACION), False)
    onda_senoidal = np.sin(FRECUENCIA_TONO * t * 2 * np.pi)
    
    audio_estereo = np.vstack((onda_senoidal, onda_senoidal)).T
    audio_data = (audio_estereo * 0.3).astype(np.float32)
    
    print("Reproduciendo por el altavoz...")
    
    sd.play(audio_data, SAMPLE_RATE, device=id_dispositivo_salida)
    sd.wait()
    
    print("¡Prueba completada con éxito!")

except Exception as e:
    print(f"\nError al reproducir el audio: {e}")

