import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array





#image load with numpy
img_path ="deneme/siyah.jpg"
img = load_img(img_path, target_size = (224, 224,3))
img = img_to_array(img)
img = np.expand_dims(img, axis = 0)


"""
import cv2
#image load with opencv
img = cv2.imread("deneme/visne.png")
img = cv2.resize(img, (224,224))
img = np.array(img, dtype="float32")
img = np.reshape(img, (1,224,224,3))
"""

#Modelin yüklenmesi ve giriş çıkış tensorlerin hazırlanması
interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()



#Giriş tensorü olarak diziye dönüştürülmüş imgenin verilmesi ve prediction işlemi
interpreter.set_tensor(input_details[0]['index'],img)
interpreter.invoke()
predictions = tf.math.softmax(interpreter.get_tensor(output_details[0]['index']))


print(predictions)



#olasılıklar arasından en büyüğünün seçilmesi ve tür eşleştirilmesi
max_index = np.argmax(predictions)

classes = ["AageanRose", "AfyonBal", "AfyonBeyaz", "AfyonBlack", "AfyonGrey", "AfyonSeker", "Bejmermer", "Blue", "Capuchino", "Diyabaz", "DolceVita", "EkvatorPijama", "ElazigVisne", "GoldGalaxy", "GulKurusu", "KaplanPostu", "Karacabeysiyah", "Konglomera", "KristalEmprador", "Leylakmermer", "MediBlack", "OliviaMarble", "Oniks", "RainGrey", "Traverten"]

print(classes[max_index])



