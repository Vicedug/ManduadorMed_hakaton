# src/automatizador.py
import time

INTERVALO = 10  # segundos (modo prueba)

print("🤖 Automatizador iniciado...")

try:
    while True:
        print("⏰ Revisando medicamentos...")
        time.sleep(INTERVALO)
except KeyboardInterrupt:
    print("\n🛑 Automatizador detenido por el usuario")
