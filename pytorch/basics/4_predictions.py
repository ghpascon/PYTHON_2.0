import torch
import torch.nn as nn
import numpy as np

def prediction_1(x=None,y=None, w=0.0, value=5, learning_rate=0.01, epochs=10):
    if(x is None or y is None):
        print('None parameter')
        return  
    #model
    def forward(x):
        return w*x

    #loss
    def loss(y, y_pred):
        return ((y_pred-y)**2).mean()
        
    #gradient
    def gradient(x,y,y_pred):
        return np.dot(2*x,y_pred-y).mean()
    

    for epoch in range(epochs):
        y_pred=forward(x)
        l=loss(y, y_pred)
        dw=gradient(x,y,y_pred)
        w-=learning_rate*dw
        print(f'Epoch {epoch+1}/{epochs}, Loss: {l}, w: {w}')

    return forward(value)


def prediction_2(x=None,y=None, w=0.0, value=5, learning_rate=0.01, epochs=10):
    if(x is None or y is None):
        print('None parameter')
        return  
    
    w=torch.tensor(w, dtype=torch.float32, requires_grad=True)
    #model
    def forward(x):
        return w*x

    #loss
    def loss(y, y_pred):
        return ((y_pred-y)**2).mean()
            

    for epoch in range(epochs):
        y_pred=forward(x)
        l=loss(y, y_pred)
        l.backward()
        with torch.no_grad():
            w-=learning_rate*w.grad
        
        w.grad.zero_()

        print(f'Epoch {epoch+1}/{epochs}, Loss: {l}, w: {w}')

    return forward(value)

def prediction_3(x=None, y=None, value=5, learning_rate=0.01, epochs=10):
    if x is None or y is None:
        print('None parameter')
        return
    
    # Convert value to tensor and reshape
    value = torch.tensor([value], dtype=torch.float32).unsqueeze(0).unsqueeze(1)

    # Get the number of features
    n_samples, n_features = x.shape

    # Define a simple linear model
    class LinearRegression(nn.Module):
        def __init__(self, input_dim, output_dim):
            super(LinearRegression, self).__init__()
            self.linear = nn.Linear(input_dim, output_dim)

        def forward(self, x):
            return self.linear(x)

    # Create model instance for a single output
    model = LinearRegression(n_features, 1)  # Output dimension is 1 for single prediction

    # Define loss function and optimizer
    loss_fn = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

    # Training loop
    for epoch in range(epochs):
        # Forward pass
        y_pred = model(x)
        loss = loss_fn(y_pred, y)
        
        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # Print progress
        weights = list(model.parameters())[0].data.numpy()
        bias = list(model.parameters())[1].data.numpy()
        print(f'Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}, Weights: {weights}, Bias: {bias}')
    
    # Predict the output for the given value
    predicted = model(value).item()
    return predicted

def main():
    # x=np.array([1,2,3,4], dtype=np.float32)
    # y=x*3

    # predicted_value = prediction_1(
    #     x=x,
    #     y=y,
    #     w=0.0,
    #     value=7,
    #     learning_rate=0.01,
    #     epochs=30
    # )

    # print(f'Predicted value: {predicted_value}')




    # x=torch.tensor([1,2,3,4,5,6,7,8,9], dtype=torch.float32)
    # y=x*3
    # predicted_value = prediction_2(
    #     x=x,
    #     y=y,
    #     w=0.0,
    #     value=33,
    #     learning_rate=0.01,
    #     epochs=100
    # )

    # print(f'Predicted value: {predicted_value}')



    x=torch.tensor([1,2,3,4,5,6,7,8,9], dtype=torch.float32)
    y=x*3
    predicted_value = prediction_3(
        x = x.unsqueeze(1) ,
        y = y.unsqueeze(1) ,
        value=33,
        learning_rate=0.03,
        epochs=1000
    )

    print(f'Predicted value: {predicted_value}')

if __name__ == "__main__":
    main()
