import torch
from torchvision import models
from torch import nn


NUM_CLASSES = 12

class BugNet(nn.Module):
    def __init__(self):
        super().__init__()

        self.net = models.resnet18(pretrained=True)
        num_fltrs = self.net.fc.in_features
        self.net.fc = nn.Linear(num_fltrs, NUM_CLASSES)

    def forward(self, x):
        predictions = self.net(x)
        return predictions