import torch
import numpy as np
from pathlib import Path
from torch.utils.data import Dataset
import deepdish as dd


class CustomDataset(Dataset):
    """Short summary.

    Parameters
    ----------
    ids_list : list
        ids list of training or validation or traning data.

    Attributes
    ----------
    ids_list

    """

    def __init__(self, ids_list):
        super(CustomDataset, self).__init__()
        self.ids_list = ids_list

    def __getitem__(self, index):
        id = self.ids_list[index]
        # Read only specific data
        path = Path(__file__).parents[2] / 'data/processed/torch_dataset.h5'
        x = dd.io.load(str(path), group='/features', sel=dd.aslice[id, :, :])
        y = dd.io.load(str(path), group='/labels', sel=dd.aslice[id, :])
        # Convert to torch tensors
        x = torch.from_numpy(x).type(torch.float32)
        y = torch.from_numpy(y).type(torch.float32)

        return x, y

    def __len__(self):
        return len(self.ids_list)