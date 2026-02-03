from flask import Flask, render_template, request, redirect, url_for
import sys
import os

# Move up two levels from src/web/app.py to reach the src/ folder
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if src_path not in sys.path:
    sys.path.append(src_path)

import gestor  # Now this will work!

app = Flask(__name__)

@app.after_request
def agregar_encabezados_sin_cache(response):
    """
    Agrega encabezados HTTP para prevenir el almacenamiento en caché.
    Esto asegura que los cambios en las recetas se reflejen inmediatamente.
    """
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/')
def pagina_inicio():
    """
    Ruta principal: Muestra el tablero con todas las recetas agrupadas.
    
    1. Carga las recetas.
    2. Agrupa por medicamento y dosis.
    3. Carga la configuración de notificaciones.
    4. Renderiza la plantilla principal.
    """
    recetas_flat = gestor.cargar_recetas()

    recetas_agrupadas = {}

    for r in recetas_flat:
        clave = f"{r['nombre'].lower().strip()}_{r['dosis'].lower().strip()}"
        if clave not in recetas_agrupadas:
            recetas_agrupadas[clave] = {
                "nombre": r['nombre'],
                "dosis": r['dosis'],
                "notas": r['notas'],
                "dosis_list": []
            }
        recetas_agrupadas[clave]["dosis_list"].append(r)

    # Ordenar cronológicamente cada grupo
    for k in recetas_agrupadas:
        recetas_agrupadas[k]["dosis_list"].sort(key=lambda x: x.get('timestamp', ''))

    config = gestor.cargar_configuracion()
    return render_template('index.html', grupos=recetas_agrupadas, config=config)

@app.route('/agregar', methods=['POST'])
def agregar():
    """
    Procesa el formulario para agregar nuevas recetas/dosis.
    """
    gestor.generar_dosis(
        request.form.get('nombre'),
        request.form.get('dosis'),
        request.form.get('hora_inicio'),
        request.form.get('frecuencia'),
        request.form.get('dias'),
        request.form.get('notas')
    )
    return redirect(url_for('pagina_inicio'))

@app.route('/configurar', methods=['POST'])
def configurar():
    """
    Guarda la configuración del Bot de Telegram.
    """
    gestor.guardar_configuracion({
        "telegram_token": request.form.get('telegram_token'),
        "telegram_chat_id": request.form.get('telegram_chat_id')
    })
    return redirect(url_for('pagina_inicio'))

@app.route('/eliminar_grupo')
def eliminar_grupo():
    """
    Elimina un grupo completo de medicamentos (todas las tomas de un tipo).
    Parámetros (query string): nombre, dosis.
    """
    nombre = request.args.get('nombre', '').strip()
    dosis = request.args.get('dosis', '').strip()

    if nombre:
        gestor.eliminar_grupo(nombre, dosis)

    return redirect(url_for('pagina_inicio'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)

