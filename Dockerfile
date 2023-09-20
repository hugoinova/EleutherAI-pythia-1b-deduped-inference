# Use a imagem base do Python
FROM python:latest

# diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install -r requirements.txt

# Copie os arquivos app.py e model.py para o contêiner
COPY app.py model.py ./

# Copie a pasta 'static' e 'templates' para o contêiner
COPY static/ ./static/
COPY templates/ ./templates/

# Exponha a porta em que o aplicativo Flask será executado
EXPOSE 5000

# Comando para iniciar o aplicativo
CMD ["python", "app.py"]
