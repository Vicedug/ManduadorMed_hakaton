from flask import Flask, request

app = Flask(__name__)

# Lista global de recordatorios (en memoria)
reminders = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        medicine = request.form.get("medicine")
        hours = request.form.get("hours").split(",")
        telegram_id = request.form.get("telegram_id")
        reminders.append({
            "medicine": medicine,
            "hours": hours,
            "telegram_id": telegram_id
        })

    html = """
    <h1>Mis Recordatorios</h1>
    <form method='POST'>
        Medicina: <input type='text' name='medicine' required><br>
        Horas (separadas por coma): <input type='text' name='hours' required><br>
        Telegram ID: <input type='text' name='telegram_id' required><br>
        <input type='submit' value='Agregar Recordatorio'>
    </form>
    <hr>
    """

    for r in reminders:
        html += f"<div style='border:1px solid black; padding:10px; margin:5px;'>"
        html += f"<b>Medicina:</b> {r['medicine']}<br>"
        html += f"<b>Horas:</b> {', '.join(r['hours'])}<br>"
        html += f"<b>Telegram ID:</b> {r['telegram_id']}</div>"

    if not reminders:
        html += "<p>No hay recordatorios</p>"

    return html

if __name__ == "__main__":
    app.run(debug=True)

