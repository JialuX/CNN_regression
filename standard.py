from PIL import Image
from pylab import *
import os
import random
import numpy as np


#path_t = r"/Users/xujialu/Desktop/Term1/Data Ming/dataset/lamem/11" #path of dataset of pics

datas = [] #dataset
train_x = []
train_y = []
valid_x = []
valid_y = []
test_x = []
test_y = []

i = 0
path_t = r"/Users/xujialu/Downloads/DATASET/training/isMem" #path of dataset of pics
for dirs in os.listdir(path_t):
    i += 1
    #if i%10== 0:
    if i < 2500:
        imgpath =os.path.join(os.path.join(path_t,dirs))
        #print(imgpath)
        img = Image.open(imgpath)
        img = img.convert('L')

        #image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        #print("size",shape(img.size))

        #conver to grey scale, and resize the pixels
        #img = img.convert('L').resize((64, 64))
        #img = img.convert('L').resize((64, 64))
        width, height = img.size
        data = np.asarray(img,dtype='float64')/256. # normalization to 0-1
        #print(data)
        #tmp = data.reshape(3, hight * width)[0]
        tmp = data.reshape(1, height * width)[0]

        tmp =hstack((dirs,tmp))  # add tag befors data
        #print(ndim(tmp))
        datas.append(tmp)
        #print("hello1")
#print("sb1",shape(datas))

i = 0
path_t = r"/Users/xujialu/Downloads/DATASET/training/isNotMem" #path of dataset of pics
for dirs in os.listdir(path_t):
    i += 1
    #if i%10== 0:
    if i < 2500:
        imgpath =os.path.join(os.path.join(path_t,dirs))
        #print(imgpath)
        img = Image.open(imgpath)
        img = img.convert('L')
        #img =img.convert('RGB').resize((28,28))
        #img = img.convert('L').resize((128, 128))
        width,height=img.size
        data = np.asarray(img,dtype='float64')/256. # standardization
        #print(data)
        #tmp = data.reshape(3, hight * width)[0]
        tmp = data.reshape(1, height * width)[0]

        tmp =hstack((dirs,tmp))  # add tag befors data
        #print(ndim(tmp))
        print("non",tmp)
        print(shape(tmp))
        datas.append(tmp)
        #print("hello1")

random.shuffle(datas)# randomly sort the dataset
#numpy.save("/Users/xujialu/Desktop/Term1/Data Ming/dataset/lamem", datas)

print("sb1",shape(datas))
np.save("/Users/xujialu/Downloads/DATASET/training", datas)





