![PetMate parte superior](/resources/PetMate.jpg)

# PetMate 🐾🤖

## Índice
1. [Descripción y Características](#descripción-y-características)
2. [Demostración](#demostración)
3. [Estructura del Repositorio](#estructura-del-repositorio)
4. [Hardware y Componentes](#hardware-y-componentes)
5. [Software y Visión Artificial](#software-y-visión-artificial)
6. [Instalación y Configuración](#instalación-y-configuración)
7. [Tareas Pendientes](#tareas-pendientes)
8. [Referencias](#referencias)
9. [Contribuidores](#contribuidores)
10. [Licencia](#licencia)

---

## Description

**PetMate** es un robot móvil autónomo e inteligente diseñado para monitorizar mascotas o animales en entornos controlados. Utilizando una **Raspberry Pi 4** y técnicas de **Visión Artificial**, el robot no solo es capaz de identificar la presencia de un animal, sino también de estimar su pose (si está de pie, sentado, tumbado o en movimiento), permitiendo entender su comportamiento en tiempo real.

---

## Características Principales

* **Detección de Animales y Poses:** Procesamiento de imágenes en tiempo real mediante la Raspberry Pi Camera Module 2.
* **Navegación Autónoma:** Sistema de evitación de obstáculos mediante 3 sensores ultrasónicos HC-SR04.
* **Eco-Friendly:** Sistema de asistencia energética mediante un panel solar integrado.
* **Interacción Activa:** Altavoz integrado para emitir sonidos o alertas basados en el comportamiento del animal.

---

## Estructura del Repositorio

* `📂 3D designs`: Modelos CAD y archivos STL para la estructura del robot.
* `📂 circuits`: Esquemas de conexión del driver L298N, sensores y Raspberry Pi.
* `📂 resources`: Diagramas de flujo, arquitectura de software y multimedia.
* `📂 src`: Código fuente en Python ejecutable en la Raspberry Pi.

---


## Arquitectura del Sistema

### Hardware (Bill of Materials)

El coste total estimado del hardware es de **191,39 €**. A continuación se detallan los componentes utilizados:

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

## Componentes

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
* *[Enlace a un tutorial, paper, o documentación que os haya servido de ayuda.]*

---

## Contribuidores
* **Junjie Liu** 
* **[Nombre Compañero]** 

---

## Licencia

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
