import cv2
import numpy as np
import matplotlib.pyplot as plt
import random as rnd
import statistics

img_path = "mermer.jpg"

img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (224,224))

img = np.array(img, dtype="float32")
img = np.reshape(img, (1,224,224,3))
randomize = img.shape[0]*img.shape[1]

renk = []
#resim yüzde 8 i kadar random piksel seçiyoruz

for i in range(int(randomize*0.08)):
    x=rnd.randint(0, img.shape[0]-1)
    y=rnd.randint(0, img.shape[1]-1)
    renk.append(img[x][y])


#Seçili random piksellerin r g b renk kodlarını başka diziye aktarıyoruz

r = []
g = []
b = []

#Ortalama bir renk kodu elde etmek için ayrıştıracağımız [r,g,b] kodlarının ortalamasını alarak renk elde ediyoruz

for a in range(len(renk)):
   r.append(renk[a][0])
   g.append(renk[a][1])
   b.append(renk[a][2])

#Elde edilen listenin ortalaması alınıyor
print("Örneğimizin rgb kodu : ",int(statistics.mean(r)),int(statistics.mean(g)),int(statistics.mean(b)))

plt.imshow(img)
plt.show()