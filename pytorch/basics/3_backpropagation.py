import torch

def main():
    x=torch.tensor(1.0)
    y=torch.tensor(2.0)

    w = torch.tensor(1.0, requires_grad=True)

    #forward_pass
    pred=w*x
    loss=(pred-y)**2
    print(loss)

    #backward_pass
    loss.backward()
    print(w.grad)

    #wpdate weights

if __name__ == "__main__":
    main()
