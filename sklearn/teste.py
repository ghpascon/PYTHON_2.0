import joblib

# Carregar o modelo e o vectorizer
model = joblib.load('model/logistic_model.pkl')
vectorizer = joblib.load('model/vectorizer.pkl')

# Função para classificar mensagens
def classify_message(message):
    vectorized_message = vectorizer.transform([message])
    prediction = model.predict(vectorized_message)[0]
    if prediction == 1:
        return "Positiva"
    elif prediction == 0:
        return "Negativa"
    elif prediction == 2:
        return "Recomendação"

# Loop para entrada do usuário
print("\nDigite uma mensagem para classificar (ou 'sair' para encerrar):")
while True:
    user_input = input("> ")  # Entrada do usuário
    if user_input.lower() == "sair":
        print("Encerrando o programa.")
        break
    result = classify_message(user_input)
    print(f"A mensagem é classificada como: {result}")
