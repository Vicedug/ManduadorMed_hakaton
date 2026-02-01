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
