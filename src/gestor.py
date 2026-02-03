import json
import os
from datetime import datetime, timedelta

# Configuración de rutas para archivos de datos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'recetas.json')
CONFIG_FILE = os.path.join(BASE_DIR, 'data', 'config.json')

def cargar_recetas():
    """
    Carga la lista de recetas desde el archivo JSON.

    Retorna:
        list: Lista de diccionarios con las recetas. Retorna lista vacía si hay error o no existe.
    """
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def guardar_recetas(recetas):
    """
    Guarda la lista de recetas en el archivo JSON.

    Argumentos:
        recetas (list): Lista de diccionarios de recetas a guardar.
    """
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(recetas, f, indent=4, ensure_ascii=False)

def cargar_configuracion():
    """
    Carga la configuración del sistema (tokens, ids, etc).

    Retorna:
        dict: Diccionario con la configuración actual.
    """
    if not os.path.exists(CONFIG_FILE):
        return {"telegram_token": "", "telegram_chat_id": ""}
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def guardar_configuracion(nuevos_datos):
    """
    Actualiza y guarda la configuración del sistema.

    Argumentos:
        nuevos_datos (dict): Datos parciales o completos para actualizar.
    """
    config_actual = cargar_configuracion()
    config_actual.update(nuevos_datos)
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config_actual, f, indent=4, ensure_ascii=False)

def generar_dosis(nombre, dosis, hora_inicio, frecuencia_horas, dias, notas=""):
    """
    Genera y guarda múltiples tomas de medicamentos basadas en una frecuencia.
    
    NOTA: Para efectos de demostración/demo:
    - La 'frecuencia_horas' se interpreta como SEGUNDOS.
    - Los 'dias' se interpretan como MINUTOS de duración total del tratamiento.

    Argumentos:
        nombre (str): Nombre del medicamento.
        dosis (str): Cantidad a tomar (ej: 500mg).
        hora_inicio (str): Hora de inicio en formato HH:MM o HH:MM:SS.
        frecuencia_horas (str/int): Intervalo entre tomas (en segundos para demo).
        dias (str/int): Duración del tratamiento (en minutos para demo).
        notas (str): Notas adicionales opcionales.

    Retorna:
        int: Número de recetas generadas.
    """
    recetas = cargar_recetas()
    nuevo_id = 1 if not recetas else max(r['id'] for r in recetas) + 1
    
    fecha_base = datetime.now().date()
    
    # Normalización de hora
    if len(hora_inicio) == 5:
        hora_inicio += ":00"
    
    try:
        hora_obj = datetime.strptime(hora_inicio, "%H:%M:%S").time()
    except ValueError:
        hora_obj = datetime.now().time()

    dt_actual = datetime.combine(fecha_base, hora_obj)
    
    # Calcular límite de tiempo (Duración del tratamiento)
    limite = dt_actual + timedelta(minutes=int(dias))
    
    nuevas_recetas = []
    
    while dt_actual < limite:
        receta = {
            "id": nuevo_id,
            "nombre": nombre,
            "dosis": dosis,
            "hora": dt_actual.strftime("%H:%M:%S"),
            "fecha": dt_actual.strftime("%d-%m-%Y"),
            "timestamp": dt_actual.strftime("%Y-%m-%d %H:%M:%S"), 
            "notas": notas
        }
        recetas.append(receta)
        nuevas_recetas.append(receta)
        nuevo_id += 1
        
        # Siguiente toma
        dt_actual += timedelta(seconds=int(frecuencia_horas))
    
    recetas.sort(key=lambda x: x.get('timestamp', ''))
    guardar_recetas(recetas)
    return len(nuevas_recetas)

def eliminar_receta(id_receta):
    """
    Elimina una receta específica por su identificador único.

    Argumentos:
        id_receta (int): ID de la receta a eliminar.

    Retorna:
        bool: True si se eliminó, False si no hubo cambios.
    """
    recetas = cargar_recetas()
    recetas_filtradas = [r for r in recetas if r['id'] != int(id_receta)]
    if len(recetas) != len(recetas_filtradas):
        guardar_recetas(recetas_filtradas)
        return True
    return False

def eliminar_grupo(nombre, dosis):
    """
    Elimina todas las recetas asociadas a un grupo de medicamento (mismo nombre y dosis).

    Argumentos:
        nombre (str): Nombre del medicamento.
        dosis (str): Dosis del medicamento.

    Retorna:
        bool: True si se eliminaron registros, False si no se encontró nada.
    """
    recetas = cargar_recetas()
    
    target_nombre = nombre.strip().lower() if nombre else ""
    target_dosis = dosis.strip().lower() if dosis else ""

    recetas_filtradas = [
        r for r in recetas 
        if not (r.get('nombre', '').strip().lower() == target_nombre and 
                r.get('dosis', '').strip().lower() == target_dosis)
    ]
    
    if len(recetas) != len(recetas_filtradas):
        guardar_recetas(recetas_filtradas)
        return True
    return False

if __name__ == "__main__":
    print("Módulo Gestor de Recetas - Ejecución de prueba")
    print(f"Recetas cargadas: {len(cargar_recetas())}")
