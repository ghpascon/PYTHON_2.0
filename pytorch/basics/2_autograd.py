import torch

def teste_1():    
    # x = torch.randn(3, requires_grad=False)
    x = torch.randn(3, requires_grad=True)
    print(x)

    y=x+2
    print(y)

    z=y*y*2
    print(z)    
    
    z=z.mean()
    print(z)

    z.backward()
    print(x.grad)

def teste_2():
    # Criar um tensor com gradientes ativados
    x = torch.tensor(2.0, requires_grad=True)

    # Realizar algumas operações
    y = x ** 2  # y = x^2
    z = y + 3   # z = x^2 + 3
    out = z * 2 # out = 2 * (x^2 + 3)

    # Imprimir o valor de 'out'
    print(out)

    # Calcular o gradiente de 'out' em relação a 'x'
    out.backward()

    # Gradiente de out em relação a x
    print("Gradiente de out em relação a x:", x.grad)

def epoch_test_1():
    weights = torch.ones(4, requires_grad=True)

    for epoch in range(5):
        model_output = (weights*3).sum()
        model_output.backward()
        print(weights.grad)

        weights.grad.zero_()

def main():
    # teste_1()
    # teste_2()
    epoch_test_1()

if __name__ == "__main__":
    main()
