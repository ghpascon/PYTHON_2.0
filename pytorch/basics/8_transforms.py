import torch
import torchvision
from torch.utils.data import Dataset, DataLoader
import numpy as np
import math

def main():
    class WineDataset(Dataset):
        def __init__(self):
            # Load the dataset
            xy = np.loadtxt('wine/wine.csv', delimiter=',', dtype=np.float32, skiprows=1)
            self.x = torch.from_numpy(xy[:, 1:])  # Features (columns 1 to end)
            self.y = torch.from_numpy(xy[:, [0]])  # Labels (first column, keep as 2D)
            self.n_samples = xy.shape[0]

        def __getitem__(self, index):
            # Return a single sample (features and label)
            return self.x[index], self.y[index]
        
        def __len__(self):
            # Return the total number of samples
            return self.n_samples
        
    # Create dataset and dataloader
    dataset = WineDataset()
    data_loader = DataLoader(dataset=dataset, batch_size=4, shuffle=True, num_workers=0)  # Set num_workers=0 for compatibility

    epochs = 3
    total_samples = len(dataset)
    iterations = math.ceil(total_samples / 4)  # Total iterations per epoch (batch size = 4)

    # Training loop (simulated)
    for epoch in range(epochs):
        for i, (inputs, labels) in enumerate(data_loader):
            print(f'Epoch {epoch+1}/{epochs}, Step {i+1}/{iterations}, Inputs Shape: {inputs.shape}, Labels Shape: {labels.shape}')


if __name__ == "__main__":
    main()
