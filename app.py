from flask import Flask, request, jsonify, render_template, send_from_directory
import model
from googletrans import Translator
import os

app = Flask(__name__)
app.debug = True  # Habilita o modo de depuração

# Defina o caminho para a pasta onde o arquivo script.js está localizado
static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

# Rota para servir arquivos estáticos (como script.js)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(static_folder, filename)

# Função para traduzir uma pergunta de português para inglês
def translate_to_english(question):
    translator = Translator()
    translated_question = translator.translate(question, src='pt', dest='en').text
    return translated_question

# Função para traduzir uma resposta de inglês para português
def translate_to_portuguese(response):
    translator = Translator()
    translated_response = translator.translate(response, src='en', dest='pt').text
    return translated_response

@app.route("/")
def index():
    # Renderiza o arquivo HTML diretamente
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form['question']

    # Traduz a pergunta de português para inglês
    translated_question = translate_to_english(question)

    # Gera a resposta em inglês
    response_in_english = model.generate_response(translated_question)

    # Traduz a resposta de inglês para português
    translated_response = translate_to_portuguese(response_in_english)

    return jsonify({"response": translated_response})

if __name__ == "__main__":
    app.run()
