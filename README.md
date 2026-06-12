<img src="resources/PetMate.jpg" align="right" width="340" alt="PetMate Robot"/>

# 🐾 PetMate

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi%204-red?logo=raspberry-pi)](https://www.raspberrypi.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Deep Learning](https://img.shields.io/badge/Deep%20Learning-YOLOv8-purple)](https://ultralytics.com/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

> **Robot autónomo inteligente** para la vigilancia, seguridad y bienestar de tus mascotas cuando no estás en casa.

PetMate patrulla tu hogar de forma autónoma, detecta y clasifica el tipo de mascota, estima su pose en tiempo real, dispensa premios por buen comportamiento y te permite interactuar con ella a distancia desde una aplicación móvil.

---

## 📋 Tabla de Contenidos

1. [Descripción General](#-descripción-general)
2. [Características Principales](#-características-principales)
3. [Demo](#-demo)
4. [Arquitectura del Sistema](#-arquitectura-del-sistema)
5. [Hardware y Componentes](#-hardware-y-componentes)
6. [Software y Visión Artificial](#-software-y-visión-artificial)
7. [Algoritmo de Navegación](#-algoritmo-de-navegación)
8. [Instalación y Configuración](#-instalación-y-configuración)
9. [Estructura del Repositorio](#-estructura-del-repositorio)
10. [Referencias](#-referencias)
11. [Contribuidores](#-contribuidores)
12. [Licencia](#-licencia)

---

## 🤖 Descripción General

**PetMate** es un robot móvil autónomo diseñado para monitorizar mascotas en entornos domésticos. Combina visión artificial, Deep Learning y navegación autónoma sobre una plataforma Raspberry Pi 4 para ofrecer:

- **Vigilancia continua** de tu mascota mientras no estás en casa.
- **Identificación** del tipo de animal y **clasificación de su pose** (de pie, sentado, tumbado, en movimiento).
- **Interacción remota** mediante una app móvil: visualización en directo y envío de audios.
- **Dispensación de premios** automática por buen comportamiento (p. ej., sentarse a la orden).
- **Patrullaje autónomo** con evasión de obstáculos mediante algoritmo *Wall Following*.
- **Autonomía energética** gracias a un panel solar integrado.

---

## ✨ Características Principales

| Característica | Detalle |
|---|---|
| 🎯 **Detección de mascotas** | Clasificación del tipo de animal en tiempo real con modelo de Deep Learning |
| 🧘 **Estimación de pose** | Detecta si la mascota está de pie, sentada, tumbada o en movimiento |
| 🗺️ **Navegación autónoma** | Algoritmo *Wall Following* con 3 sensores ultrasónicos HC-SR04 |
| 🚧 **Evasión de obstáculos** | Detección frontal, izquierda y derecha para esquivar obstáculos dinámicos |
| 📱 **App remota** | Streaming de vídeo en directo y control de audio desde el móvil |
| 🔊 **Altavoz integrado** | Reproducción de audios enviados desde la app o alertas automáticas |
| 🍖 **Dispensador de premios** | Servo-actuado: dispensa una chuche cuando detecta la secuencia correcta de comportamiento |
| ☀️ **Panel solar** | Recarga continua para vigilancia prolongada sin necesidad de enchufar el robot |
| ☁️ **Modelo en la nube** | Inferencia y almacenamiento gestionados remotamente mediante el proyecto *PetWatch* |

---

## 🎬 Demo

> 📹 **[Ver vídeo del robot en funcionamiento](#)** ← *(añade aquí el enlace al vídeo)*

---

## 🏗️ Arquitectura del Sistema

```
┌─────────────────────────────────────────────────────┐
│                    APLICACIÓN MÓVIL                 │
│          (Streaming vídeo · Envío de audios)         │
└────────────────────┬────────────────────────────────┘
                     │ WiFi / Cloud (PetWatch)
┌────────────────────▼────────────────────────────────┐
│                  RASPBERRY PI 4                      │
│                                                     │
│  ┌─────────────┐   ┌──────────────┐  ┌───────────┐ │
│  │  Pi Camera  │──▶│ Deep Learning│  │  PetWatch │ │
│  │  Module 2   │   │  (Detección  │─▶│   Cloud   │ │
│  └─────────────┘   │  + Pose Est.)│  └───────────┘ │
│                    └──────┬───────┘                 │
│  ┌─────────────┐          │ Comportamiento           │
│  │ HC-SR04 ×3  │   ┌──────▼───────┐  ┌───────────┐ │
│  │ (Izq·Frente │──▶│  Navegación  │  │Dispensador│ │
│  │    ·Der.)   │   │Wall Following│  │  (Servo)  │ │
│  └─────────────┘   └──────┬───────┘  └───────────┘ │
│                           │                         │
│  ┌─────────────┐   ┌──────▼───────┐  ┌───────────┐ │
│  │ Panel Solar │   │   L298N +    │  │ Altavoz   │ │
│  │ + PowerBank │   │  2× Motores  │  │  3W       │ │
│  └─────────────┘   └──────────────┘  └───────────┘ │
└─────────────────────────────────────────────────────┘
```

---

## 🔧 Hardware y Componentes

El coste total estimado del hardware es de **213,33 €**.

| Imagen | Componente | Unid. | Precio |
|:---:|:---|:---:|---:|
| ![Raspberry Pi 4](resources/componentes/raspberry-pi-4-modelo-b-8gb-ram.jpg) | Raspberry Pi 4 Modelo B — 8 GB RAM | 1 | 88,50 € |
| ![Pi Camera](resources/componentes/camara-raspberry-pi-v2-8-megapixels.jpg) | Raspberry Pi Camera Module 2 (8 MP) | 1 | 19,95 € |
| ![PowerBank](resources/componentes/PowerBank.jpg) | PowerBank 10 000 mAh | 1 | 33,59 € |
| ![L298N](resources/componentes/controlador-de-motores-doble-puente-h-l298.jpg) | Controlador de motores doble puente H — L298N | 1 | 15,50 € |
| ![Micrófono](resources/componentes/microfono-digital-mems-i2s-sph0645.jpg) | Micrófono electret preamplificado | 1 | 9,75 € |
| ![Panel Solar](resources/componentes/panel-solar-6v-1w-con-cable.jpg) | Panel Solar 6 V / 1 W con cable | 1 | 7,90 € |
| ![Ruedas](resources/componentes/pareja-de-ruedas-80x10mm-blanco.jpg) | Pareja de ruedas 80×10 mm | 1 | 7,95 € |
| ![Altavoz](resources/componentes/altavoz-con-caja-3w.jpg) | Altavoz con caja 3 W | 1 | 5,90 € |
| ![Servo](resources/componentes/micro-servo-sg90-rotacion-continua.jpg) | Servo MG90S (dispensador) | 1 | 3,95 € |
| ![Motor](resources/componentes/motor-micro-metal-dc-con-reductora.jpg) | Motor Micro Metal LP con reductora | 2 | 4,50 € |
| ![Pilas](resources/componentes/pila-alcalina-4-x-aa.jpg) | Pilas Alcalinas 4×AA | 1 | 2,99 € |
| ![Base pilas](resources/componentes/base-para-baterias-4xaa.jpg) | Base para pilas 4×AA | 1 | 2,00 € |
| ![HC-SR04](resources/componentes/sensor-de-distancia-por-ultrasonidos-hc-sr04.jpg) | Sensor ultrasónico HC-SR04 | 3 | 1,80 € |
| ![LDR](resources/componentes/fotoresistencia-ldr.jpg) | Fotoresistor LDR | 1 | 0,95 € |
| | | **TOTAL** | **213,33 €** |

---

## 🧠 Software y Visión Artificial

El pipeline de visión artificial se estructura en dos etapas en cascada:

### 1. Detección del tipo de mascota
- Modelo de detección de objetos entrenado con técnicas de **Deep Learning**.
- Procesa el flujo de vídeo en tiempo real desde la **Pi Camera Module 2**.
- Clasifica el animal detectado (perro, gato, etc.).

### 2. Estimación de pose
Una vez identificado el animal, un segundo modelo clasifica su estado postural:

| Pose | Descripción |
|---|---|
| 🧍 De pie | El animal está erguido sobre sus patas |
| 🪑 Sentado | El animal está sentado |
| 🛌 Tumbado | El animal está estirado en el suelo |
| 🏃 En movimiento | El animal se desplaza activamente |

### Infraestructura Cloud — PetWatch
El modelo de inferencia está desplegado en la nube a través del proyecto **[PetWatch](📂 PetWatch)**, que también gestiona:
- Streaming de vídeo hacia la app móvil.
- Recepción y reproducción de audios enviados por el usuario.
- Almacenamiento de eventos y alertas.

**Stack tecnológico:** *(completa aquí con los frameworks y librerías usadas, p. ej. YOLOv8, TensorFlow Lite, OpenCV, Flask…)*

---

## 🗺️ Algoritmo de Navegación

PetMate implementa un algoritmo de **Wall Following** para patrullar el hogar de forma estructurada:

```
┌─────────────────────────────────────────────────────────────┐
│                   LÓGICA DE NAVEGACIÓN                      │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Sensor DERECHO detecta pared                         │   │
│  │                                                      │   │
│  │  · Demasiado cerca  →  Ajustar: girar a la izquierda │   │
│  │  · Distancia ideal  →  Seguir recto                  │   │
│  │  · Demasiado lejos  →  Ajustar: girar a la derecha   │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Sensor FRONTAL detecta obstáculo  →  Girar izquierda │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Sin pared detectada  →  Girar izquierda hasta        │   │
│  │                          encontrar pared por derecha  │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

El robot mantiene siempre una pared a su **derecha**, recorriendo el perímetro de las habitaciones de forma sistemática. Los tres sensores HC-SR04 (frontal, izquierdo, derecho) permiten detectar y esquivar obstáculos dinámicos como muebles o personas.

---

## 🚀 Instalación y Configuración

### Requisitos previos

- Raspberry Pi 4 con Raspberry Pi OS (64-bit)
- Python 3.11+
- Conexión WiFi activa

### Dependencias principales

```bash
pip install opencv-python
pip install numpy
pip install RPi.GPIO
# (añade aquí el resto de librerías del proyecto)
```

### Pasos de instalación

**1. Clonar el repositorio:**

```bash
git clone https://github.com/TU_USUARIO/PetMate.git
cd PetMate
```

**2. Instalar dependencias:**

```bash
pip install -r requirements.txt
```

**3. Configurar credenciales de la nube (PetWatch):**

```bash
cp config/config.example.yaml config/config.yaml
# Edita config.yaml con tus credenciales
```

**4. Ejecutar el robot:**

```bash
python src/main.py
```

---

## 📂 Estructura del Repositorio

```
PetMate/
│
├── 📂 3D designs/       # Modelos CAD y archivos STL de la estructura del robot
├── 📂 PetWatch/         # Módulo de visión por computador y servidor en la nube
├── 📂 circuits/         # Esquemas de conexión: L298N, sensores y Raspberry Pi
├── 📂 src/              # Código fuente Python ejecutable en la Raspberry Pi
│   ├── main.py          #   Punto de entrada principal
│   ├── navigation.py    #   Algoritmo Wall Following
│   ├── detection.py     #   Pipeline de visión artificial
│   ├── dispenser.py     #   Control del dispensador (servo)
│   └── cloud.py         #   Comunicación con PetWatch
└── 📂 resources/        # Diagramas, arquitectura, fotos de componentes
```

---

## 📚 Referencias

- *Wall Following Algorithm for Mobile Robots* — *(añade referencia académica)*
- *YOLOv8 / Deep Learning framework utilizado* — *(añade referencia)*
- [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/)
- [HC-SR04 Ultrasonic Sensor Datasheet](https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf)

---

## 👥 Contribuidores

| Nombre | GitHub |
|---|---|
| Junjie Liu | [@usuario](#) |
| Joel Rillo Fernández | [@usuario](#) |
| Gerard Saez Salat | [@usuario](#) |
| Elías Pascual Paz | [@usuario](#) |

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

















![PetMate parte superior](/resources/PetMate.jpg)

# PetMate 🐾🤖
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Hardware](https://img.shields.io/badge/Hardware-Raspberry%20Pi%204-red.svg)
![AI](https://img.shields.io/badge/AI-Deep%20Learning%20%7C%20Computer%20Vision-blue.svg)

Proyecto de robótica móvil enfocado en la vigilancia, seguridad y bienestar de tus mascotas en entornos domésticos.

[🔗 Enlace al vídeo de demostración del robot] (Añade aquí tu link)

---

## 📑 Tabla de Contenidos
1. [¿Qué es PetMate?](#qué-es-petmate)
2. [Características Principales](#características-principales)
3. [Navegación y Algoritmos](#navegación-y-algoritmos)
4. [Estructura del Repositorio](#estructura-del-repositorio)
5. [Hardware y Componentes (BOM)](#hardware-y-componentes-bom)
6. [Instalación y Configuración](#instalación-y-configuración)
7. [Contribuidores](#contribuidores)
8. [Licencia](#licencia)

---

## 🐶 ¿Qué es PetMate?

**PetMate** es un robot móvil autónomo e inteligente diseñado para monitorizar mascotas en entornos controlados. Alimentado por una **Raspberry Pi 4**, el robot está conectado a un servidor en la nube que aloja un modelo de **Deep Learning** entrenado con técnicas de Visión Artificial. 

A través de una aplicación móvil, los dueños pueden conectarse en tiempo real para ver lo que capta la cámara del robot, interactuar mediante audio y asegurarse de que sus animales están seguros, todo mientras el robot patrulla la casa de forma completamente autónoma.

---

## ✨ Características Principales

* **Detección de Animales y Estimación de Pose:** Procesamiento de imágenes en tiempo real mediante la Raspberry Pi Camera Module 2. El modelo no solo reconoce el tipo de mascota, sino que clasifica su estado (sentado, tumbado, de pie, etc.).
* **Interacción Remota (App y Cloud):** Conexión a la nube que permite retransmitir el vídeo en directo a una aplicación móvil. Puedes enviar audios desde la app que el robot reproducirá a través de su altavoz integrado.
* **Dispensador Inteligente de Premios:** Si le ordenas a tu mascota que se siente a través del altavoz y el modelo de IA detecta la pose "sentado", el robot dispensa automáticamente una chuche/premio.
* **Patrullaje Autónomo Anticolisión:** Sistema avanzado de evasión de obstáculos y seguimiento de paredes utilizando 3 sensores ultrasónicos HC-SR04 y un controlador de motores L298N.
* **Asistencia Eco-Friendly:** Panel solar integrado para prolongar la autonomía de la batería mientras estás fuera de casa.

---

## 🧠 Navegación y Algoritmos

### Algoritmo *Wall Following* (Seguimiento de Paredes)
PetMate utiliza un algoritmo inteligente para patrullar tu casa garantizando la cobertura del espacio sin quedarse atascado:

1. **Seguimiento Continuo:** El robot mantiene siempre la pared a su derecha asegurándose de que el sensor ultrasónico derecho detecte una superficie.
2. **Ajuste de Distancia:** Si se acerca demasiado a la pared lateral, corrige su trayectoria suavemente mediante los motores.
3. **Evasión Frontal:** Si el sensor frontal detecta un obstáculo o esquina, el robot lo esquiva.
4. **Búsqueda de Paredes:** En espacios abiertos donde el sensor derecho pierde la pared, el robot gira sobre sí mismo hacia la izquierda hasta volver a encontrarla. Si los muros están muy lejos, avanza en línea recta hasta que el sensor frontal detecte el siguiente obstáculo para reanudar la ruta.

### Arquitectura de Visión Artificial
El cerebro visual del robot (`📂 PetWatch`) se apoya en modelos de Deep Learning exportados a la nube, permitiendo liberar carga de procesamiento a la Raspberry Pi 4 mientras mantiene la latencia al mínimo para la detección de poses.

---

## 🗂️ Estructura del Repositorio

* `📂 3D designs`: Modelos CAD y archivos STL para la estructura del robot y el dispensador de premios.
* `📂 PetWatch`: Código del proyecto de Visión por Computadores y conexión con el servidor en la nube.
* `📂 circuits`: Esquemas de conexión del driver L298N, sensores y Raspberry Pi.
* `📂 resources`: Diagramas de flujo, arquitectura de software, componentes y piezas del robot.
* `📂 src`: Código fuente en Python ejecutable en la Raspberry Pi.

---

## 🛠️ Hardware y Componentes (BOM)

El coste total estimado del hardware es de **213,33 €**. A continuación se detallan los componentes utilizados:

| Imagen | Descripción | Uds. | Precio | 
| :--- | :--- | :--- | :--- |
| ![Foto resistor](/resources/componentes/fotoresistencia-ldr.jpg) | Foto resistor | 1 | 0,95 € |
| ![Ultrasonido](/resources/componentes/sensor-de-distancia-por-ultrasonidos-hc-sr04.jpg) | Sensor Ultrasónico HC-SR04 | 3 | 1,80 € |
| ![Panel Solar](/resources/componentes/panel-solar-6v-1w-con-cable.jpg) | Panel Solar | 1 | 7,90 € |
| ![Servo MG90S](/resources/componentes/micro-servo-sg90-rotacion-continua.jpg) | Servo MG90S (Rotación Continua) | 1 | 3,95 € |
| ![Altavoz](/resources/componentes/altavoz-con-caja-3w.jpg) | Altavoz con caja / 3 W | 1 | 5,90 € |
| ![Raspberry Pi](/resources/componentes/raspberry-pi-4-modelo-b-8gb-ram.jpg) | Raspberry Pi 4 Modelo B 8GB RAM | 1 | 88,50 € |
| ![Micrófono](/resources/componentes/microfono-digital-mems-i2s-sph0645.jpg) | Micrófono electret preamplificado | 1 | 9,75 € |
| ![Controlador](/resources/componentes/controlador-de-motores-doble-puente-h-l298.jpg) | Controlador puente H-L298N | 1 | 15,50 € |
| ![Cámara](/resources/componentes/camara-raspberry-pi-v2-8-megapixels.jpg) | Raspberry Pi Camera Module 2 | 1 | 19,95 € |
| ![PowerBank](/resources/componentes/PowerBank.jpg) | PowerBank 10k mAh | 1 | 33,59 € |
| ![Ruedas](/resources/componentes/pareja-de-ruedas-80x10mm-blanco.jpg) | Pareja de ruedas 80x10mm - Blanco | 1 | 7,95 € |
| ![Motor](/resources/componentes/motor-micro-metal-dc-con-reductora.jpg) | Motor Micro Metal LP | 2 | 4,50 € |
| ![Base pilas](/resources/componentes/base-para-baterias-4xaa.jpg) | Base para pilas 4xAA | 1 | 2,00 € |
| ![Pilas](/resources/componentes/pila-alcalina-4-x-aa.jpg) | Pilas Alcalinas 4xAA | 1 | 2,99 € |
| **TOTAL** | | | **213,33 €** |

*(Nota: Adicionalmente, se requiere material de impresión 3D para la carcasa externa y el mecanismo del dispensador de comida).*

---

## 🚀 Instalación y Configuración

Sigue estos pasos para desplegar el código en la Raspberry Pi 4 del robot:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/PetMate.git](https://github.com/TU_USUARIO/PetMate.git)
   cd PetMate
   
2. **Instalar dependencias de Python:**
   Recomendamos crear un entorno virtual para las librerías de visión y control de motores.
   ```bash
   pip install -r requirements.txt
   
3. **Ejecutar el nodo principal:**
   Recomendamos crear un entorno virtual para las librerías de visión y control de motores.
   ```bash
   pip install -r requirements.txt








































![PetMate parte superior](/resources/PetMate.jpg)
Proyecto de robótica enfocado en la vigilancia, seguridad y bienestar de tus mascotas. 
link video robot

### Tabla de contenidos
1. [Descripción y Características](#descripción-y-características)
2. [Demostración](#demostración)
3. [Estructura del Repositorio](#estructura-del-repositorio)
4. [Hardware y Componentes](#hardware-y-componentes)
5. [Software y Visión Artificial](#software-y-visión-artificial)
6. [Instalación y Configuración](#instalación-y-configuración)
7. [Referencias](#referencias)
8. [Contribuidores](#contribuidores)
9. [Licencia](#licencia)

---

## Description

**PetMate** es un robot móvil autónomo e inteligente diseñado para monitorizar mascotas o animales en entornos controlados utilizando un modelo entrenado por técnicas de Visión Artificial y DeepLearning para que pueda detectar y reconocer los tipos de mascotas. Además, el robot no solo es capaz de identificar la presencia de un animal, sino también de estimar su pose (si está de pie, sentado, tumbado o en movimiento), permitiendo entender su comportamiento en tiempo real. De esta forma podrás tener vigilado y controlado a tus mascotas cuando no estés en casa para su tranquilidad. 

Utilizando una **Raspberry Pi 4** 

---

## Características Principales

* **Detección de Animales y Poses:** Procesamiento de imágenes en tiempo real mediante la Raspberry Pi Camera Module 2.
* **Navegación Autónoma:** Sistema de evitación de obstáculos mediante 3 sensores ultrasónicos HC-SR04.
* **Eco-Friendly:** Sistema de asistencia energética mediante un panel solar integrado.
* **Interacción Activa:** Altavoz integrado para emitir sonidos o alertas basados en el comportamiento del animal.

---

## Estructura del Repositorio

* `📂 3D designs`: Modelos CAD y archivos STL para la estructura del robot.
* `📂 PetWatch`: Github al proyecto de Visión por Computadores y servidor en la nube.
* `📂 circuits`: Esquemas de conexión del driver L298N, sensores y Raspberry Pi.
* `📂 resources`: Diagramas de flujo, arquitectura de software, componentes y piezas del robot.
* `📂 src`: Código fuente en Python ejecutable en la Raspberry Pi.

---


## Arquitectura del Sistema

### Hardware (Bill of Materials)

El coste total estimado del hardware es de **213,33 €**. A continuación se detallan los componentes utilizados:

## Lista de componentes
| Imagen | Descripción | Unidades | Precio | 
| :--- | :--- | :--- | :---
| ![Foto resistor](/resources/componentes/fotoresistencia-ldr.jpg) | Foto resistor | 1 | 0,95 € |
| ![Ultrasonido_HC-SR04](/resources/componentes/sensor-de-distancia-por-ultrasonidos-hc-sr04.jpg) | HC-SR04 | 3 | 1,80 € |
| ![Panel Solar](/resources/componentes/panel-solar-6v-1w-con-cable.jpg) | Panel Solar | 1 | 7,90 € |
| ![Servo MG90S](/resources/componentes/micro-servo-sg90-rotacion-continua.jpg) | Servo MG90S | 1 | 3,95 € |
| ![Altavoz con caja / 3 W](/resources/componentes/altavoz-con-caja-3w.jpg) | Altavoz con caja / 3 W | 1 | 5,90 € |
| ![Raspberry Pi 4 Modelo B 8GB RAM](/resources/componentes/raspberry-pi-4-modelo-b-8gb-ram.jpg) | Raspberry Pi 4 Modelo B 8GB RAM | 1 | 88,50 € |
| ![Micrófono](/resources/componentes/microfono-digital-mems-i2s-sph0645.jpg) | Micrófono electret preamplificado | 1 | 9,75 € |
| ![Controlador de motores](/resources/componentes/controlador-de-motores-doble-puente-h-l298.jpg) | Controlador de motores doble puente H-L298N | 1 | 15,50 € |
| ![Raspberry Pi Camera Module 2](/resources/componentes/camara-raspberry-pi-v2-8-megapixels.jpg) | Raspberry Pi Camera Module 2 | 1 | 19,95 € |
| ![PowerBank](/resources/componentes/PowerBank.jpg) | PowerBank 10k mha | 1 | 33,59 € |
| ![Pareja de ruedas 80x10mm](/resources/componentes/pareja-de-ruedas-80x10mm-blanco.jpg) | Pareja de ruedas 80x10mm - Blanco | 1 | 7,95 € |
| ![Motor Micro Metal](/resources/componentes/motor-micro-metal-dc-con-reductora.jpg) | Motor Micro Metal LP | 2 | 4,50 € |
| ![Base baterias 4xAA](/resources/componentes/base-para-baterias-4xaa.jpg) | Base para pilas 4xAA | 1 | 2 € |
| ![Pilas Alcalinas 4xAA](/resources/componentes/pila-alcalina-4-x-aa.jpg) | Pilas Alcalinas 4xAA | 1 | 2,99 € |
| TOTAL | | | 213,33 € |

---

### Software & Modelos

(qué usamos para todo lo de VC)

---

## Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/PetMate.git](https://github.com/TU_USUARIO/PetMate.git)
   cd PetMate

---

## Referencias
* *...*

---

## Contribuidores
* **Junjie Liu** 
* **Joel Rillo Fernández**
* **Gerard Saez Salat**
* **Elías Pascual Paz**

---

## Licencia

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
