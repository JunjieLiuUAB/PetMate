import os
import sys
import time
import threading

os.environ["GPIOZERO_PIN_FACTORY"] = "lgpio"

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SRC_DIR)
PETWATCH_CLIENT_DIR = os.path.join(ROOT_DIR, "PetWatch-G2_5-main", "backend", "edge_client")

if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)
if PETWATCH_CLIENT_DIR not in sys.path:
    sys.path.append(PETWATCH_CLIENT_DIR)

from src.dispenser_servo import dar_comida
from src.navigation import iniciar_navegacion_autonoma

try:
    from conectar_camara import main as iniciar_streaming_camara
    from escuchador_audio import coleccion_audio_ref, reproducir_audio
    CLOUD_AVAILABLE = True
except ImportError as e:
    print(\f"⚠️ No se pudieron cargar módulos de PetWatch. Verifica los nombres de archivos. Error: {e}")
    CLOUD_AVAILABLE = False

def main():
    print("==============================================")
    print("        INICIANDO ECOCONEXIÓN PETMATE         ")
    print("==============================================")

    sistema_activo = threading.Event()
    sistema_activo.set()

    HILOS = []

    hilo_motores = threading.Thread(
        target=iniciar_navegacion_autonoma, 
        args=(sistema_activo,), 
        name="Hilo-Navegacion"
    )
    hilo_motores.daemon = True 
    HILOS.append(hilo_motores)

    if CLOUD_AVAILABLE:
        hilo_camara = threading.Thread(
            target=iniciar_streaming_camara, 
            name="Hilo-Camara"
        )
        hilo_camara.daemon = True
        HILOS.append(hilo_camara)
        
        print("[SISTEMA] Conectando escuchador asíncrono de Firestore...")
        observador_firestore = coleccion_audio_ref.on_snapshot(reproducir_audio)

    for hilo in HILOS:
        print(f"[SISTEMA] Arrancando: {hilo.name}")
        hilo.start()

    print("\n[OK] Todo el ecosistema está en marcha de forma síncrona.")
    print("Presiona Ctrl + C para apagar el robot de forma segura.\n")

    try:
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\n🛑 [APAGADO] Solicitud de parada manual detectada.")
    finally:
        print("[APAGADO] Desactivando banderas y deteniendo actuadores...")
        sistema_activo.clear() 
        if CLOUD_AVAILABLE:
            print("[APAGADO] Removiendo observador de Firebase...")
            observador_firestore.unsubscribe()
        time.sleep(0.5)
        print("[OK] Robot PetMate apagado de forma segura.")

if __name__ == "__main__":
    main()
