import transformers

# Carrega modelo pré-treinado
model = transformers.AutoModelForCausalLM.from_pretrained("EleutherAI/pythia-1b-deduped")
tokenizer = transformers.AutoTokenizer.from_pretrained("EleutherAI/pythia-1b-deduped")

# Função para fazer inferência e gerar resposta
def generate_response(question):
    # Pré-processa
    question = question.lower().replace('\n', ' ')

    # Tokeniza
    inputs = tokenizer(question, return_tensors="pt")

    # Faz inferência e limita a 50 palavras ou tokens
    outputs = model.generate(**inputs, max_length=50, num_return_sequences=1)

    # Decodifica resposta
    response = tokenizer.decode(outputs[0])

    # Faz pós-processamento
    response = response.replace('<pad>', '')
    response = response.replace('</s>', '')
    response = response.replace('<s>', '')
    response = response.strip()

    return response
