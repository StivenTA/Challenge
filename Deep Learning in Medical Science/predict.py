from keras.models import load_model
from keras.utils import load_img,img_to_array
from keras.applications.vgg16 import preprocess_input
import numpy as np

IMG_PATH = 'Dataset/val/PNEUMONIA/person1950_bacteria_4881.jpeg'
model = load_model('model_vgg16.h5',compile=False)
img = load_img(IMG_PATH, target_size=(224, 224))
# print(img)
array = img_to_array(img)
array = np.expand_dims(array, axis=0)
img_data = preprocess_input(array)
prediction = model.predict(img_data)

print(prediction)