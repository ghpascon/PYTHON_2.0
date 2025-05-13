import matplotlib.pyplot as plt
from sklearn import datasets

# Carregar o dataset de dígitos
digits = datasets.load_digits()

# Informações sobre o dataset
print("Tamanho do dataset:", len(digits.data))
print("Formato de cada entrada (imagem achatada):", digits.data[0].shape)
print("Classes disponíveis:", digits.target_names)

# Exibir os 10 primeiros números
plt.figure(figsize=(10, 4))
for i in range(10):
    # Criar subplots para exibir as imagens
    plt.subplot(2, 5, i + 1)
    plt.imshow(digits.images[i], cmap="gray")  # A imagem no formato 8x8
    plt.title(f"Número: {digits.target[i]}")
    plt.axis("off")

plt.tight_layout()
plt.show()
