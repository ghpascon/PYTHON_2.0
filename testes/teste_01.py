import numpy as np
from sklearn.linear_model import LinearRegression

# Gerar entradas aleatórias
num_inputs = 50  # Quantidade de números aleatórios
x = np.random.randint(1, 500, size=(num_inputs, 1))  # Números inteiros entre 1 e 500

# Definir a relação y = 4x + x/3
y = x * 4 + x / 3

# Criar o modelo de regressão linear
modelo = LinearRegression()

# Treinar o modelo
modelo.fit(x, y)

# Novos inputs para prever
novo_inputs = np.array([[3], [7], [9], [20]])  # Array 2D com novos valores
previsoes = modelo.predict(novo_inputs)

# Exibir os resultados
print("Novos inputs e suas previsões:")
for entrada, predicao in zip(novo_inputs.flatten(), previsoes.flatten()):
    print(f"Input: {entrada} -> Previsão: {predicao:.2f}")
