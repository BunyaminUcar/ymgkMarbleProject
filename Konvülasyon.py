

"""
# Örnek veriler
X = np.array([[[0,0,0],
               [0,0,0],
               [0,1,0]],
              [[0,0,0],
               [0,2,1],
               [0,2,1]]])

w0 = np.array([[[-1,0,1],
                [0,0,1],
                [1,-1,1]],
               [[-1,0,1],
                [1,-1,1],
                [0,1,0]]])

w1 = np.array([[[0,1,-1],
                [0,-1,0],
                [0,-1,1]],
               [[-1,0,0],
                [1,-1,0],
                [1,-1,0]]])

b0 = 1
b1 = 0

# Konvülasyon işlemi

# İlk filtre
O0 = np.zeros((2,2))
for i in range(2):
  for j in range(2):
    for k in range(2):
      for l in range(3):
        for m in range(3):
          if i+l < 3 and j+m < 3:
            O0[i,j] += X[k,i+l,j+m] * w0[k,l,m]
    O0[i,j] += b0

# İkinci filtre
O1 = np.zeros((2,2))
for i in range(2):
  for j in range(2):
    for k in range(2):
      for l in range(3):
        for m in range(3):
          i"f i+l < 3 and j+m < 3:
            O1[i,j] += X[k,i+l,j+m] * w1[k,l,m"]
    O1[i,j] += b1

# Sonuçlar
print(O0)
print(O1)

"""


"""
#####
import numpy as np
# Örnek veriler
# X = 7*7*3 matris oluştur
X=np.array([[[0,0,0,0,0,0,0],
             [0,0,0,1,0,2,0],
             [0,1,0,2,0,1,0],
             [0,1,0,2,2,0,0],
             [0,2,0,0,2,0,0],
             [0,2,1,2,2,0,0],
             [0,0,0,0,0,0,0]],
            [[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,1,0,0,0,0],
             [0,2,-1,1,0,0,0],
             [0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]],
            [[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]])


# filter w0 (3*3*3)
w0 = np.array([[[1,0,1],
                [0,0,0],
                [1,0,1]],
                [[1,0,1],
                [0,0,0],
                [1,0,1]],
                [[1,0,1],
                [0,0,0],
                [1,0,1]]])

# filter w1 (3*3*3)
w1 = np.array([[[1,1,1],
                [0,0,0],
                [1,1,1]],
                [[1,1,1],
                [0,0,0],
                [1,1,1]],
                [[1,1,1],
                [0,0,0],
                [1,1,1]]])

# bias
b0 = 1
b1 = 0

# Konvülasyon işlemi

# İlk filtre
O0 = np.zeros ((5,5))


print(O0)"""


"""
import numpy as np

# Öncelikle, 5x5x3 lük matrisimizi oluşturalım
matrix = np.random.rand(5, 5, 3)

# Konvülsiyon için filtremizi belirleyelim
filter = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])

# Matrisimizi filtremiz ile konvülve edelim
convolved_matrix = np.zeros((3, 3, 3))
for i in range(3):
    for j in range(3):
        for k in range(3):
            convolved_matrix[i][j][k] = np.sum(matrix[i:i+3, j:j+3, k] * filter)

# Konvülsiyon sonucu elde edilen matrisi görelim
print(convolved_matrix)
"""

                     
import numpy as np

# Giriş verisi
x=np.array([[[0,0,0,0,0,0,0],
             [0,0,0,1,0,2,0],
             [0,1,0,2,0,1,0],
             [0,1,0,2,2,0,0],
             [0,2,0,0,2,0,0],
             [0,2,1,2,2,0,0],
             [0,0,0,0,0,0,0]],
            [[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,1,0,0,0,0],
             [0,2,-1,1,0,0,0],
             [0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]],
            [[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]])

# Konvülasyon katmanları
w0 = np.array([[[-1, 0, 1],
                [0, 0, 1],
                [1, -1, 1]],
               [[-1,0,1],
                [1,-1,1],
                [0,1,0]],
               [[-1,1,1],
                [1,1,0],
                [0,-1,0]]])

w1 = np.array([[[0,1,-1],
                [0,-1,0],
                [0,-1,1]],
               [[-1,0,0],
                [1,-1,0],
                [1,-1,0]]])

# Bias değerleri
bias0 = 1
bias1 = 0

# Konvülasyon işleminin sonucu
result = np.zeros((x.shape[0], x.shape[1] - w0.shape[1] + 1, x.shape[2] - w0.shape[2] + 1, 2))

# Konvülasyon işlemini gerçekleştir
for i in range(result.shape[0]):
    for j in range(result.shape[1]):
        for k in range(result.shape[2]):
            result[i, j, k, 0] = np.sum(x[i, j:j+w0.shape[1], k:k+w0.shape[2]] * w0) + bias0
            result[i, j, k, 1] = np.sum(x[i, j:j+w1.shape[1], k:k+w1.shape[2]] * w1) + bias1

print(result)












