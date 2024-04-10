import google.generativeai as genai
from flask import Flask, request, jsonify


app = Flask(__name__)

GOOGLE_API_KEY = 'AIzaSyCkDYC9tkqDlliBUnEgmEGAtOV6gS7I5-k'
genai.configure(api_key=GOOGLE_API_KEY)

@app.route('/')
def home():
    return "Web Service Gemini responses"

@app.route('/chat_direcciones', methods=['POST'])
def chat_direcciones():
    data = request.json
    pregunta_inicial = data.get("pregunta")
    id_conversacion = data.get("id_conversacion", None) # pruebas, esto podria ser opcional

    model = genai.GenerativeModel('gemini-pro')

    if not id_conversacion or id_conversacion == "nueva":
        chat = model.start_chat(history=[])
        chat.send_message("Dame la dirección exacta y precisa de lugares en la ciudad de México de acuerdo a Google Maps.")
    else:
        historial = [] 
        chat = model.start_chat(history=historial)

    respuesta_detallada = chat.send_message("Dame la dirección exacta en una linea " + pregunta_inicial)

    return jsonify({"respuesta": respuesta_detallada.text, "id_conversacion": "19DJ1L20"})

@app.route('/chat_matematicas', methods = ['POST'])
def chat_matematicas():
    data = request.json
    pregunta_inicial = data.get("pregunta")
    id_conversacion = data.get("id_conversacion", None)

    model = genai.GenerativeModel('gemini-pro')

    if not id_conversacion or id_conversacion == "nueva":
        chat = model.start_chat(history=[])
        # Dar el contexto relacionado a preguntas sobre matemáticas
        chat.send_message("Eres profesor de educación básica en matemáticas y das respuestas precisas.")
    else:
        historial = []
        chat = model.start_chat(history=historial)

    respuesta_detallada = chat.send_message("Explica en tres lineas " + pregunta_inicial)

    return jsonify({"respuesta": respuesta_detallada.text, "id_conversacion": "20DJ1L20"})

@app.route('/chat_general', methods = ['POST'])
def chat_general():
    data = request.json
    pregunta_inicial = data.get("pregunta")
    id_conversacion = data.get("id_conversacion", None)

    model = genai.GenerativeModel('gemini-pro')

    if not id_conversacion or id_conversacion == "nueva":
        chat = model.start_chat(history=[])
        # Dar el contexto relacionado a preguntas sobre cosas generales
        chat.send_message("Das respuestas de cultura general de educación básica.")
    else:
        historial = []
        chat = model.start_chat(history=historial)

    respuesta_detallada = chat.send_message("Explica en en cuatro lineas " + pregunta_inicial)

    return jsonify({"respuesta": respuesta_detallada.text, "id_conversacion": "21DJ1L20"})


if __name__ == '__main__':
    app.run(debug=True)

