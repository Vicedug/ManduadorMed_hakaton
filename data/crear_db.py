'''
crear_db deberia funcionar como un modulo que separamos del resto de la logica de manipulación de archivos pues
su proposito principal es de crear la base de datos, siendo una funcion que solo es ejecutada una vez en la
carpeta correcta y como funcion auxiliar devolver la conección a esa base de datos, modularizacón, estructura 
e implementación de bases de datos esta abierta a cambios

'''
# python -m venv venv
# .\venv\Scripts\activate


import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "healthcare.db"


def get_connection():
    """Return a connection with foreign keys enabled."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    """Run once to create tables."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            client_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS medications (
            med_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            dosage TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS schedules (
            schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER,
            med_id INTEGER,
            hour TEXT NOT NULL,
            FOREIGN KEY (client_id) REFERENCES clients (client_id),
            FOREIGN KEY (med_id) REFERENCES medications (med_id)
        )
    """)

    conn.commit()
    conn.close()
    print(f"Database initialized at: {DB_PATH}")
