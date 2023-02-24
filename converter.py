import tensorflow as tf

model = tf.keras.models.load_model('bestmodel.h5', compile=True)
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.post_training_quantize = True
tflite_model = converter.convert()
open("model3.tflite", "wb").write(tflite_model)

