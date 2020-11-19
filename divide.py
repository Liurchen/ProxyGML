import os
import scipy.io as sio
from os import path
import shutil

MAT_PATH = "/home/rc/Downloads/datasets/ProxyGML_datasets/cars_annos.mat"

mat = sio.loadmat(MAT_PATH)


def mkdir(path: str) -> bool:
    if exists(path):
        return True
    else:
        try:
            os.mkdir(path)
        except OSError:
            return False
        else:
            return True


def exists(pth: str) -> bool:
    return path.exists(pth)


def mv(src: str, dst: str) -> bool:
    shutil.copy(src, dst)


for line in mat.items():
    if line[0] == 'annotations':
        for i in range(len(line[1][0])):
            label = line[1][0][i][5][0][0]
            img = line[1][0][i][0][0]
            src = "/home/rc/Downloads/datasets/ProxyGML_datasets/" + img
            dst = "/home/rc/Documents/ProxyGML/data/car_ims/" + \
                str(label)
            if not exists(dst):
                mkdir(dst)
            mv(src, dst)
