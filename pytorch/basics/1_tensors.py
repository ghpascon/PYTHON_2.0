import torch
import numpy as np

def basics():
    x = torch.empty(3)
    print(x)    
    x = torch.rand(2,2)
    print(x)    
    x = torch.zeros(3,3,3)
    print(x)
    x = torch.tensor([2.5, 1, 0.99])
    print(x)

def operations():
    x= torch.rand(2,2)
    y= torch.rand(2,2)

    print(x)
    print(y)

    z=x+y
    print(z)

    w=x-y
    print(w)

def show():
    x = torch.rand(2,2)
    print(x)  
    print(x[0,0])  
    print(x[:,0])  
    print(x[0,:])  

def in_place():
    # Criando o tensor inicial
    x = torch.tensor([2.5, 1, 0.99])
    print("Tensor inicial:", x)

    # Operações NÃO in-place (criam um novo tensor)
    print("\n=== Operações NÃO in-place ===")
    y = x.add(5)
    print("add (não in-place):", y)

    y = x.sub(3)
    print("sub (não in-place):", y)

    y = x.mul(2)
    print("mul (não in-place):", y)

    y = x.div(2)
    print("div (não in-place):", y)

    y = x.pow(2)
    print("pow (não in-place):", y)

    y = x.clamp(0, 2)
    print("clamp (não in-place):", y)

    # Tensor original permanece inalterado
    print("Tensor original após operações NÃO in-place:", x)

    # Operações IN-PLACE (modificam o tensor original)
    print("\n=== Operações IN-PLACE ===")
    x.add_(5)
    print("add_ (in-place):", x)

    x.sub_(3)
    print("sub_ (in-place):", x)

    x.mul_(2)
    print("mul_ (in-place):", x)

    x.div_(2)
    print("div_ (in-place):", x)

    x.pow_(2)
    print("pow_ (in-place):", x)

    x.clamp_(10, 15)
    print("clamp_ (in-place):", x)

def main():
    basics()
    operations()
    show()
    in_place()

if __name__ == "__main__":
    main()
