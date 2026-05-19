# PetMate

## Table of Content
- Description
- Components
- Software

## Description


## List of Components
| Name | Units | Price | 
| :--- | :--- | :---
| Foto resistor | 1 | 0,95 € |
| HC-SR04 | 3 | 1,80 € |
| Panel Solar | 1 | 7,90 € |
| Servo MG90S | 1 | 3,95 € |
| Altavoz 40mm / 3 W | 1 | 5,90 € |
| Raspberry Pi 4 Modelo B 8GB RAM | 1 | 88,50 € |
| Micrófono electret preamplificado | 1 | 9,75 € |
| Controlador de motores doble puente H-L298N | 1 | 15,50 € |
| Raspberry Pi Camera Module 2 | 1 | 19,95 € |
| PowerBank Anker Nano 30 W | 1 | 33,59 € |
| TOTAL |  | 191,39 € |

## Components

# PetMate 🐾🤖

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**PetMate** es un robot móvil autónomo e inteligente diseñado para monitorizar mascotas o animales en entornos controlados. Utilizando una **Raspberry Pi 4** y técnicas de **Visión Artificial**, el robot no solo es capaz de identificar la presencia de un animal, sino también de estimar su pose (si está de pie, sentado, tumbado o en movimiento), permitiendo entender su comportamiento en tiempo real.

---

## 🚀 Características Principales

* **Detección de Animales y Poses:** Procesamiento de imágenes en tiempo real mediante la Raspberry Pi Camera Module 2.
* **Navegación Autónoma:** Sistema de evitación de obstáculos mediante 3 sensores ultrasónicos HC-SR04.
* **Eco-Friendly:** Sistema de asistencia energética mediante un panel solar integrado.
* **Interacción Activa:** Altavoz integrado para emitir sonidos o alertas basados en el comportamiento del animal.

---

## 🛠️ Arquitectura del Sistema

### Hardware (Bill of Materials)

El coste total estimado del hardware es de **191,39 €**. A continuación se detallan los componentes utilizados:

| Componente | Unidades | Precio Estimado |
| :--- | :---: | :---: |
| Raspberry Pi 4 Modelo B 8GB RAM | 1 | 88,50 € |
| PowerBank Anker Nano 30 W | 1 | 33,59 € |
| Raspberry Pi Camera Module 2 | 1 | 19,95 € |
| Controlador de motores doble puente H-L298N | 1 | 15,50 € |
| Micrófono electret preamplificado | 1 | 9,75 € |
| Panel Solar | 1 | 7,90 € |
| Altavoz 40mm / 3 W | 1 | 5,90 € |
| Servo MG90S | 1 | 3,95 € |
| Sensor Ultrasónico HC-SR04 | 3 | 1,80 € |
| Foto resistor (LDR) | 1 | 0,95 € |
| **TOTAL** | | **191,39 €** |

> 📌 *Nota: Los diseños de las piezas de la estructura para impresión 3D se encuentran en la carpeta `/3D designs`.*

### Software & Modelos

*(Añade aquí brevemente qué usáis para la visión artificial, por ejemplo: OpenCV, TensorFlow Lite, MediaPipe, etc.)*

---

## 📂 Estructura del Repositorio

* `📂 3D designs`: Modelos CAD y archivos STL para la estructura del robot.
* `📂 circuits`: Esquemas de conexión del driver L298N, sensores y Raspberry Pi.
* `📂 resources`: Diagramas de flujo, arquitectura de software y multimedia.
* `📂 src`: Código fuente en Python ejecutable en la Raspberry Pi.

---

## 📦 Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/PetMate.git](https://github.com/TU_USUARIO/PetMate.git)
   cd PetMate
