import torch
import torch.nn as nn
import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt  # Correct import for plotting

def main():
    # Load breast cancer dataset
    bc = datasets.load_breast_cancer()
    x = bc.data
    y = bc.target

    n_samples, n_features = x.shape
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1234)

    # Standardize the data
    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)

    # Convert to torch tensors
    x_train = torch.from_numpy(x_train.astype(np.float32))
    x_test = torch.from_numpy(x_test.astype(np.float32))
    y_train = torch.from_numpy(y_train.astype(np.float32))
    y_test = torch.from_numpy(y_test.astype(np.float32))

    # Reshape y to be a column vector
    y_train = y_train.unsqueeze(1)
    y_test = y_test.unsqueeze(1)

    # Define Logistic Regression Model
    class LogisticRegression(nn.Module):
        def __init__(self, n_input_features):
            super(LogisticRegression, self).__init__()
            self.linear = nn.Linear(n_input_features, 1)

        def forward(self, x):
            return torch.sigmoid(self.linear(x))  # Fix return statement

    # Initialize model, criterion, and optimizer
    learning_rate = 0.3
    model = LogisticRegression(n_features)
    criterion = nn.BCELoss()  # Binary Cross Entropy loss
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

    # Training loop
    epochs = 1000
    for epoch in range(epochs):
        y_pred = model(x_train)
        loss = criterion(y_pred, y_train)  # Correct loss calculation
        loss.backward()

        optimizer.step()
        optimizer.zero_grad()

        print(f'Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}')

    # Evaluate on the test set
    with torch.no_grad():
        y_pred = model(x_test)
        y_pred_cls = y_pred.round()  # Round to get binary predictions (0 or 1)

        correct = (y_pred_cls == y_test).sum().item()  # Count correct predictions
        total = y_test.size(0)  # Total number of samples
        accuracy = (correct / total) * 100  # Calculate accuracy
        print(f'Accuracy on test set: {accuracy:.2f}%')

if __name__ == "__main__":
    main()
