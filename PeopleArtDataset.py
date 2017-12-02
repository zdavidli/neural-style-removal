import numpy as np
import os.path
import torchvision.datasets as dset
from torch.utils.data import DataLoader, Dataset
import torchvision.transforms as transforms
from PIL import Image

im_folder = dset.ImageFolder(root="./PeopleArt50-master/JPEGImages")

train = np.loadtxt("./PeopleArt50-master/Annotations/person_train.txt", dtype="str", ndmin=2)
test = np.loadtxt("./PeopleArt50-master/Annotations/person_test.txt", dtype="str", ndmin=2)

def peopleart_loader(path):
    with open(os.path.join("./PeopleArt50-master/JPEGImages", path), 'rb') as f:
        with Image.open(f) as img:
            return img.convert('RGB')

class PeopleArtDataset(Dataset):
    def __init__(self, train, transform=None):
        self.transform = transform
        self.train = train

    def __getitem__(self, index):
        if self.train:
            im = peopleart_loader(train[index][0])
            label = int(train[index][1])

        else:
            im = peopleart_loader(test[index][0])
            label = int(test[index][1])

        if self.transform is not None:
            im = self.transofmr(im)

        return im, label

    def __len__(self):
        if self.train:
            return train.shape[0]
        return test.shape[0]
