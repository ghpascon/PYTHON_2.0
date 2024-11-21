import torch
import torch.nn as nn
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt  # Correct import for plotting

def main():
    # Generate regression dataset
    x_numpy, y_numpy = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=1)
    
    # Convert to PyTorch tensors
    x = torch.from_numpy(x_numpy.astype(np.float32))
    y = torch.from_numpy(y_numpy.astype(np.float32))
    y = y.unsqueeze(1)  # Reshaping y to match the model's output shape

    # Get the number of samples and features
    n_samples, n_features = x.shape

    # Define the model
    model = nn.Linear(n_features, 1)

    # Define the loss function and optimizer
    criterion = nn.MSELoss()
    learning_rate = 0.01
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)  # Correct optimizer initialization

    # Training loop
    epochs = 100
    for epoch in range(epochs):
        # Forward pass
        y_pred = model(x)
        loss = criterion(y_pred, y)
        
        # Backward pass
        loss.backward()
        
        # Update the model parameters
        optimizer.step()
        
        # Zero the gradients for the next iteration
        optimizer.zero_grad()

        # Print progress
        print(f'Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}')

    # Get the predicted values
    predicted = model(x).detach().numpy()

    # Plotting the results
    plt.scatter(x_numpy, y_numpy, color='red')  # Plot the original data
    plt.plot(x_numpy, predicted, color='blue')  # Plot the regression line
    plt.show()

if __name__ == "__main__":
    main()
