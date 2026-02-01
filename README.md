# ManduadorMed_hakaton
Se crea este repositorio para trabajar en conjunto por el proyecto de la hakaton_5.0. Se trata de un script que manda mensajes recordatorios a los usuarios.
## Contexto y Problemática Social
El envejecimiento poblacional es una realidad global. Con la edad, aumenta la prevalencia de enfermedades crónicas que requieren polifarmacia (uso de múltiples medicamentos). Un problema crítico en la geriatría es la **falta de adherencia terapéutica**: los pacientes olvidan sus dosis, las confunden o las repiten, lo que conlleva descompensaciones, hospitalizaciones evitables y un deterioro en la calidad de vida.

Este proyecto propone una solución híbrida (Web de Gestión + Automatización de Escritorio) diseñada específicamente para reducir la brecha digital y asegurar la continuidad del tratamiento.

## Impacto y Utilidad por Actores

### 1. Para el Paciente (Adulto Mayor)
*   **Independencia y Dignidad:** Permite al usuario mantener el control de su salud sin depender constantemente de que otra persona le diga qué hacer en el momento exacto.
*   **Accesibilidad Cognitiva:** Al usar un sistema de "Automatización Pasiva", el paciente **no necesita interactuar con la tecnología** para recibir el beneficio. No requiere logins, contraseñas ni navegación. El sistema "va" hacia ellos mediante alertas de voz (Text-to-Speech) y ventanas emergentes claras.
*   **Reducción de Errores:** Minimiza el riesgo de olvidar una dosis o tomar una doble por error, actuando como una memoria externa fiable.

### 2. Para los Familiares y Cuidadores
*   **Gestión Simplificada (Interfaz Web):** La interfaz Web permite que hijos o enfermeros carguen y organicen el esquema de medicación de forma rápida y centralizada, sin tener que interactuar con archivos de configuración complejos.
*   **Tranquilidad Mental:** Reduce la carga mental de estar pendiente del reloj ("carga del cuidador"), sabiendo que un sistema robusto avisará al paciente.
*   **Flexibilidad:** Permite modificar dosis o horarios fácilmente tras una visita médica, asegurando que el paciente siempre tenga la pauta actualizada.

### 3. Para los Médicos y Profesionales de la Salud
*   **Eficacia Terapéutica:** La mejor medicina no funciona si no se toma. Este sistema asegura que el tratamiento prescrito se siga tal cual fue diseñado, mejorando los outcomes clínicos.
*   **Estandarización:** Facilita que las indicaciones (nombre, miligramos, horario) se trasladen de la receta de papel a un sistema digital estructurado, reduciendo la ambigüedad en el hogar.

## Conclusión
Más que un simple recordatorio, este proyecto es una **herramienta de asistencia sanitaria** que utiliza la tecnología para humanizar el cuidado, devolviendo autonomía al paciente y brindando soporte logístico a su red de apoyo.

1. Diseño de Carpetas

<img width="838" height="709" alt="Captura de pantalla 2026-01-31 223611" src="https://github.com/user-attachments/assets/503ec53a-c5d1-40ed-a6c6-1c239702421b" />

2. Flujo del Sistema (Paso a Paso)
   
El sistema funciona en un bucle continuo conectando estos componentes:

Fase A: Configuración (Usuario -> Sistema)
Entrada: El usuario abre el navegador y va a la web local.
Proceso: 
src/web/app.py
 recibe los datos (ej: "Tomar Ibuprofeno a las 14:00").
Almacenamiento: 
app.py
 usa funciones de 
src/gestor.py
 para guardar esta información en los archivos dentro de la carpeta data/.

Fase B: Monitoreo (Sistema en Segundo Plano)
Vigilancia: El script 
src/automatizador.py
 se ejecuta constantemente (bucle infinito).
Consulta: Cada minuto, pregunta a 
src/gestor.py
: "¿Hay alguna medicina programada para esta hora exacta?".
Decisión: Si la respuesta es SÍ, pasa a la fase de notificación.

Fase C: Acción (Sistema -> Usuario)
Ejecución: 
src/automatizador.py
 llama a 
src/notificador.py
.
Salida: 
notificador.py
 ejecuta las acciones configuradas:
Envía un mensaje a Telegram usando el token de 
config.json
.

Plan de Distribución de Trabajo por Arquitectura


1. Rol: Desarrollador Backend (El "Motor") Responsables: Rodrigo Segovia, Juan Manuel Ayala, Daniel Valdez
Enfoque: Lógica de negocio, manejo de datos y automatización en segundo plano.

Carpeta de Trabajo: src/ (raíz) y data/
Archivos Responsables:
src/gestor.py
: Crear funciones CRUD (Crear, Leer, Actualizar, Borrar) para las recetas. Asegurar que los datos se guarden bien en persistencia.
src/automatizador.py
: Programar el bucle infinito eficiente. Asegurar que no consuma mucha CPU y que compare bien las horas.
src/notificador.py
: Implementar la conexión con API de Telegram.
data/config.json
: Definir la estructura de configuración que usará el sistema.


2. Rol: Desarrollador Frontend / Web (La "Cara") Responsables: Victor E. Gonzalez, Anita Escurra
Enfoque: Interfaz gráfica para el usuario (cuidadores/familiares) y experiencia de usuario (UX).

Carpeta de Trabajo: src/web/
Archivos Responsables:
src/web/templates/: Diseñar los HTMLs. Que sean claros, botones grandes (accesibilidad), formularios fáciles de usar.
src/web/static/: CSS para que se vea bien y JS para interactividad simple en el navegador.
src/web/app.py: Crear las rutas (@app.route). Importante: Este rol debe coordinar con el Backend para usar las funciones de gestor.py correctamente desde aquí.


3. Rol: QA & Testing (El "Control de Calidad") Responsables: Juan Gonzalez, Kevin Bello, Anita Escurra
Enfoque: Asegurar que nada falle y que las integraciones funcionen.

Carpeta de Trabajo: src/ (Scripts de prueba)
Archivos Responsables:
src/test_telegram.py: Crear scripts aislados para verificar que las claves de API funcionan y los mensajes llegan.
Pruebas de Integración: Verificar el flujo completo: Crear receta en Web -> Verificar que se guarda en Data -> Verificar que Automatizador la detecta.

4. Rol: DevOps / Integrador (El "Armador") Responsables: Rodrigo Segovia, Juan Manuel Ayala, Daniel Valdez
Enfoque: Puesta en marcha, documentación y facilidad de instalación.

Carpeta de Trabajo: Raíz y docs/
Archivos Responsables:
requirements.txt: Mantener las versiones de librerías actualizadas y compatibles.
run.bat: Asegurar que el script de inicio levante tanto el servidor web como el automatizador (quizás en procesos paralelos).
docs/: Mantener la documentación al día para que cualquier nuevo desarrollador entienda el proyecto.


Resumen de Flujo de Trabajo Sugerido

Backend define la estructura de datos en gestor.py.
Frontend crea las pantallas en src/web/ usando la estructura definida.
Backend implementa la lógica de alertas en automatizador.py en paralelo.
QA escribe tests para validar notificador.py independientemente.
Integrador junta todo en main.py o run.bat y verifica.
