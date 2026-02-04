# src/gestor.py

# Lista que simula la "base de datos" de medicinas
medicamentos = []

def agregar_medicamento(nombre, dosis, horarios):
    medicamento = {
        "nombre": nombre,
        "dosis": dosis,
        "horario": horarios
    }
    medicamentos.append(medicamento)
    return medicamento

def obtener_todos():
    return medicamentos

