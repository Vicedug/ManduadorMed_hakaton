# ManduaMed_hakaton
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
Estructura de Carpetas
A continuación, se muestra cómo están organizados los archivos en tu proyecto:

Proyecto H5
data/
docs/
src/
.venv/
config.json
PyWhatKit_DB.txt
fundamentacion_proyecto.md
web/
main.py
automatizador.py
gestor.py
notificador.py
Tests scripts...
app.py
templates/
static/
Flujo de Funcionamiento
Este diagrama explica cómo se conectan las partes lógica (Python) con la interfaz (Web) y el usuario.

Interfaz Web (Gestión): El usuario (familiar/cuidador) usa la web para cargar las recetas.
Base de Datos/Archivos: La Web guarda estos datos (probablemente en JSON o BD gestionada por 
gestor.py
).
El "Cerebro" (Automatizador): 
automatizador.py
 se ejecuta en segundo plano (o lanzado por 
main.py
). Lee periódicamente los datos para saber cuándo toca una medicación.
Notificación: Cuando es la hora, usa 
notificador.py
 para enviar alertas (Telegram/WhatsApp/Audio).
Automatización (Paciente)
Lógica del Sistema
Interfaz de Gestión (Familiar)
1. Carga Receta
2. Guarda Datos
3. Escribe
4. Consulta Horarios
5. Lee
6. Detecta Hora
7. Alerta de Voz
8. Mensaje
Navegador Web
src/web/app.py
src/gestor.py
Datos/JSON
src/automatizador.py
src/notificador.py
Altavoces/Escritorio
Telegram API
Descripción de Componentes Clave
src/web/app.py
: El servidor web (Flask). Aquí es donde defines las rutas (/agregar, /lista, etc.) y renderizas las plantillas HTML para que el usuario interactúe.
src/gestor.py
: El intermediario. Probablemente contiene funciones como cargar_recetas(), guardar_receta(), etc. Sirve para que tanto la Web como el Automatizador hablen el mismo idioma y no toquen los archivos "crudos" directamente.
src/automatizador.py
: El script que "nunca duerme" (o que se ejecuta regularmente). Revisa constantemente si la hora actual coincide con alguna hora de medicación guardada.
src/notificador.py
: El especialista en mensajería. Sabe cómo hablar con la API de Telegram o cómo usar librerías para enviar mensajes de WhatsApp o reproducir sonidos.
