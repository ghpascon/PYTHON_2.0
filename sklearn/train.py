import os
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Mensagens positivas
positive_messages = [
    "Excelente",
    "Maravilhoso",
    "Muito bom",
    "Amei",
    "Fantástico",
    "Sensacional",
    "Perfeito",
    "Nota 10",
    "Super recomendo",
    "Surpreendente",
    "Impressionante",
    "Top",
    "Incrível",
    "Adorei",
    "Ótima experiência",
    "Melhor impossível",
    "Satisfação garantida",
    "Cumpre o prometido",
    "Tudo perfeito",
    "Altamente recomendado",
    "Super recomendo",
    "Recomendo",
    "entrega muito rapida",
    "Chegou bem rapido",
]

# Mensagens negativas
negative_messages = [
    "Ruim",
    "Péssimo",
    "Defeito",
    "Demora",
    "Devagar",
    "Insatisfatório",
    "Fraco",
    "Desapontante",
    "Decepcionante",
    "Inaceitável",
    "Horrível",
    "Problema",
    "Falho",
    "Errado",
    "Mal feito",
    "Desagradável",
    "Perda de tempo",
    "Não recomendo",
    "Ruim demais",
    "Sem qualidade",
    "Demora",
    "Demorou muito",
    "Entrega demorada",
]

# Mensagens de recomendação
recommendation_messages = [
    "Poderia",
    "Deveriam",
    "Se fizessem",
    "Seria bom",
    "Seria interessante",
    "Recomendo que",
    "Aconselho que",
    "Sugiro que",
    "Vale a pena considerar",
    "Seria útil",
    "É importante que",
    "Considerem",
    "Seria melhor",
    "Seria vantajoso",
    "Podem tentar",
    "Vale a pena",
    "Seria interessante se",
    "Poderiam melhorar",
    "Se possível, poderiam",
]

# Juntar as mensagens e criar os rótulos
messages = positive_messages + negative_messages + recommendation_messages
labels = [1] * len(positive_messages) + [0] * len(negative_messages) + [2] * len(recommendation_messages)

# Transformar texto em vetores numéricos
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)

# Criar o modelo de classificação (Regressão Logística)
model = LogisticRegression(multi_class='ovr', max_iter=1000)

# Treinar o modelo
model.fit(X_train, y_train)

# Verificar se a pasta 'model' existe, se não, criar
if not os.path.exists('model'):
    os.makedirs('model')

# Salvar o modelo treinado e o vetorizer
joblib.dump(model, 'model/logistic_model.pkl')
joblib.dump(vectorizer, 'model/vectorizer.pkl')

print("Modelo treinado e salvo com sucesso!")
