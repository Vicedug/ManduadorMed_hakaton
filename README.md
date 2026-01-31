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




##Proyecto 
|-- data/                       (Datos persistentes)
|   |-- config.json             (Configuración: tokens, teléfonos)
|   |-- PyWhatKit_DB.txt        (Base de datos interna de librería)
|
|-- docs/                       (Documentación)
|   |-- fundamentacion_proyecto.md (Explicación del proyecto)
|
|-- src/                        (Código Fuente Principal)
|   |-- web/                    (Componente: Interfaz Web)
|   |   |-- templates/          (Archivos HTML: index.html, etc.)
|   |   |-- static/             (CSS, JS, imágenes públicas)
|   |   |-- app.py              (Servidor Web Flask: Rutas web)
|   |
|   |-- main.py                 (Punto de entrada principal)
|   |-- automatizador.py        (Cerebro: Chequea horarios y lanza tareas)
|   |-- gestor.py               (Lógica: Maneja datos, lee/escribe archivos)
|   |-- notificador.py          (Salida: Envía Telegram)
|   |-- test_telegram.py        (Scripts de prueba...)
|   |-- test_whatsapp.py
|
|-- .venv/                      (Entorno Virtual de Python)
|-- requirements.txt            (Lista de librerías necesarias)
|-- run.bat                     (Script para iniciar todo con un clic)
2. Flujo del Sistema (Paso a Paso)
El sistema funciona en un bucle continuo conectando estos componentes:

