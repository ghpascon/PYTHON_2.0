from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

# Carregar o dataset Iris
data = load_iris()
X = data.data  # Atributos (features)
y = data.target  # Classes (labels)

# Dividir os dados em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criar e treinar o modelo
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_train, y_train)

# Fazer previsões
previsoes = modelo.predict(X_test)

# Exibir a árvore de decisão em formato de texto
tree_rules = export_text(modelo, feature_names=data.feature_names)
print("Regras da Árvore de Decisão:")
print(tree_rules)

# Avaliar a precisão do modelo
from sklearn.metrics import accuracy_score
precisao = accuracy_score(y_test, previsoes)
print(f"\nA precisão do modelo é: {precisao:.2f}")
