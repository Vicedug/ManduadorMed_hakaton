from gestor import agregar_medicamento, obtener_todos

agregar_medicamento(
    nombre="Ibuprofeno",
    dosis="400mg",
    horarios=["08:00", "20:00"]
)

print(obtener_todos())

