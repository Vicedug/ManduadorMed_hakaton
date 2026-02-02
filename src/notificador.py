'''
Implementar logica de enviar mensajes para que esos mensajes sean enviados en automatizador.py
'''
# python -m src.notificador


import tkinter as tk
from tkinter import messagebox
import threading
import requests  # Import moved to top

# Keep tkinter and threading for now

def mostrar_popup(titulo, mensaje):
    """
    Muestra una ventana emergente que bloquea el flujo hasta que se cierra.
    Se ejecuta en un hilo separado para no congelar el automatizador.
    """
    def _show():
        # Crear ventana oculta raíz
        root = tk.Tk()
        root.withdraw()
        # Asegurar que la ventana aparezca encima de todo
        root.attributes('-topmost', True)
        
        # Sonido de alerta nativo
        root.bell()
        
        # Mostrar mensaje
        messagebox.showinfo(titulo, mensaje)
        
        root.destroy()

    # Ejecutar en hilo aparte para no detener el reloj
    threading.Thread(target=_show).start()



def enviar_telegram(token, chat_id, mensaje):
    """
    Envía mensaje vía Telegram Bot API.
    Es silencioso, rápido y no requiere foco.
    """
    if not token or not chat_id:
        print("Telegram no configurado (Falta Token o Chat ID).")
        return

    print(f"--- Envinado a Telegram ({chat_id}) ---")
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": mensaje,
            "parse_mode": "Markdown"
        }
        # Timeout para que no cuelgue el automatizador si no hay internet
        response = requests.post(url, data=data, timeout=10)
        
        if response.status_code == 200:
            print("✅ Telegram enviado correctamente.")
        else:
            print(f"❌ Fallo Telegram: {response.text}")
    except Exception as e:
        print(f"❌ Error conexión Telegram: {e}")

if __name__ == "__main__":
    print("Probando notificador...")