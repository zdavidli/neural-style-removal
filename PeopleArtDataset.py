from torch.utils.data import Dataset, DataLoader
from PIL import Image
import os

class PeopleArtDataset(Dataset):
    
    def __init__(self, root="../PeopleArt-master/JPEGImages", train=True, transform=None):
        self.root = root
        self.transform = transform
        self.train = train
        if self.train:
            self.files = np.loadtxt("../PeopleArt-master/Annotations/person_train.txt", dtype='str', ndmin=2)
        else:
            self.files = np.loadtxt("../PeopleArt-master/Annotations/person_test.txt", dtype='str', ndmin=2)
            
#         print(self.files)
    
    def __len__(self):
        return self.files.shape[0]

    def __getitem__(self, idx):
        im_name = self.files[idx]
        im = Image.open(os.path.join(self.root, im_name[0]))
        label = int(int(im_name[1]) > 0)
        
        if self.transform:
            im = self.transform(im)
#         print(im_name)    
        return im, label
    
class PeopleArtPhotoDataset(Dataset):
    #Gets photos, no labels
    def __init__(self, root="../PeopleArt-master/JPEGImages/photo", transform=None):
        self.root = root
        self.transform = transform
        self.files =  [files for r,d,files in os.walk(self.root)][0]

    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):
        im_name = self.files[idx]
        im = Image.open(os.path.join(self.root, im_name))
        if self.transform:
            im = self.transform(im)
        return im