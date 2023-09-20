# EleutherAI-pythia-1b-deduped-inference
Inferencia em modelo "EleutherAI/pythia-1b-deduped", tradução portgues-ingles, user interface. 

## Estrutura do Projeto

O projeto está organizado da seguinte maneira:

- **static**: Diretório para arquivos estáticos JavaScript(css feito com bootstrap)
- **templates**: Diretório para arquivos de modelos HTML usados pelo Flask para renderizar página de pergunta.
- **app.py**: O código-fonte principal da aplicação Flask, servidor.
- **model.py**:  contém implementações do modelo, funcionalidades como tradução, max_lenght (tamanho da resposta).
- **requirements-comments.txt**:  Dependências do projeto.

## Requisitos de Instalação

Para executar este projeto localmente, você precisará das seguintes dependências Python:

- Flask
- Transformers
- torch
- Googletrans
  ##Deixei pois vai ser necessário para o finetune
- python-dotenv
- requests
- nltk

Recomendo criar um ambiente virtual para isolar as dependências do projeto. Você pode usar a ferramenta `virtualenv` para isso.

```bash
# Crie um ambiente virtual (certifique-se de estar na raiz do projeto)
python -m venv venv

# Ative o ambiente virtual (dependendo do seu sistema operacional)
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

# Instale as dependências a partir do requirements.txt
pip install -r requirements-comments.txt
# Executando o Projeto
Para iniciar a aplicação, você pode usar o seguinte comando:

python app.py
A aplicação estará disponível em http://localhost:5000
