import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

# Definir a transformação para normalizar os dados
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

# Baixar e carregar os dados de treino e teste
trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=False)

# Definir a estrutura da rede neural
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 128)   # Camada de entrada (28x28 pixels = 784 entradas)
        self.fc2 = nn.Linear(128, 64)        # Camada oculta
        self.fc3 = nn.Linear(64, 10)         # Camada de saída (10 classes)

    def forward(self, x):
        x = x.view(-1, 28 * 28)              # Redimensionar para vetor
        x = torch.relu(self.fc1(x))          # ReLU na primeira camada
        x = torch.relu(self.fc2(x))          # ReLU na segunda camada
        x = self.fc3(x)                      # Saída final
        return x

# Instanciar o modelo, função de perda e otimizador
net = SimpleNet()
criterion = nn.CrossEntropyLoss()           # Função de perda para classificação
optimizer = optim.SGD(net.parameters(), lr=0.01)  # Otimizador Stochastic Gradient Descent (SGD)

# Treinar o modelo
epochs = 5
for epoch in range(epochs):  # loop de treinamento
    running_loss = 0.0
    for images, labels in trainloader:
        optimizer.zero_grad()               # Zera os gradientes dos parâmetros

        outputs = net(images)               # Forward pass
        loss = criterion(outputs, labels)   # Calcula a perda
        loss.backward()                     # Backward pass
        optimizer.step()                    # Atualiza os pesos

        running_loss += loss.item()
    print(f"Epoch [{epoch + 1}/{epochs}], Loss: {running_loss/len(trainloader):.4f}")
print("Treinamento finalizado!")

# Avaliar o modelo
correct = 0
total = 0
with torch.no_grad():  # Não precisamos calcular gradientes durante a avaliação
    for images, labels in testloader:
        outputs = net(images)
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f'Acurácia no conjunto de teste: {100 * correct / total:.2f}%')
