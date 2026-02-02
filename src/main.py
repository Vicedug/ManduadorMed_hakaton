'''
Main ejecuta todo como su nombre indica, "prende" el sitio y la logica de backend
frontend -> logica base de datos (gestor) -> logica de mandar mensaje (notificador) -> logica de repeticion (automatizacion)
'''
# python -m src.main
# Usar este formato par modularizacion correcta, desde la raiz del proyecto, corregir y ver uso adecuado

import subprocess
import webbrowser
import time
import requests
import sys
import os


def start_server():
    print("[Launcher] Starting Web Server...")
    # Using python directly assuming it's in path
    return subprocess.Popen(["python", "src/web/app.py"], shell=True)

def start_automation():
    print("[Launcher] Starting Automation Engine...")
    return subprocess.Popen(["python", "src/automatizador.py"], shell=True)

def wait_for_server(url, timeout=30):
    print(f"[Launcher] Waiting for server at {url}...")
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("[Launcher] Server is UP!")
                return True
        except requests.ConnectionError:
            pass
        time.sleep(1)
    return False



def main():
    print("--- ManduadorMed Launcher ---")
    
    # Paths assuming launcher.py is in root
    if not os.path.exists("src/web/app.py"):
        print("Error: Could not find src/web/app.py. Are you running from project root?")
        sys.exit(1)

    # Start processes
    server_process = start_server()
    automation_process = start_automation()
    
    SERVER_URL = "http://127.0.0.1:5000"
    
    # Wait for server to be ready
    if wait_for_server(SERVER_URL):
        print(f"[Launcher] Opening browser at {SERVER_URL}")
        webbrowser.open(SERVER_URL)
    else:
        print("[Launcher] Timeout waiting for server. Please check console for errors.")
    
    print("\n[Launcher] System running. Press Ctrl+C to stop.")
    
    try:
        while True:
            time.sleep(1)
            # Basic check if processes are still alive
            if server_process.poll() is not None:
                print("[Launcher] Web Server stopped unexpectedly.")
                break
            if automation_process.poll() is not None:
                print("[Launcher] Automation Engine stopped unexpectedly.")
                break
    except KeyboardInterrupt:
        print("\n[Launcher] Stopping services...")
    finally:
        server_process.terminate()
        automation_process.terminate()
        print("[Launcher] Exiting.")

if __name__ == "__main__":
    main()
