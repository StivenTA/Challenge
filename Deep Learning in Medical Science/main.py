#Using data from: https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia

#Library Needed: keras, Tenserflow, Numpy, Mathplotlib
from keras.layers import Input,Lambda, Dense, Flatten
from keras.models import Model
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
import numpy as np
from glob import glob
import matplotlib.pyplot as plt

#Image size for resizing
IMAGE_SIZE = [224,224]

#path file for train and test data
train_path = "Dataset/train"
test_path = "Dataset/test"

#Preprocessing layer
vgg = VGG16(input_shape=IMAGE_SIZE + [3], weights='imagenet',include_top=False)

# not train the existing weights
for layer in vgg.layers:
    layer.trainable = False

#getting number of classes
folders = glob("Dataset/train/*")

x = Flatten()(vgg.output)

prediction = Dense(len(folders),activation='softmax')(x)

model = Model(inputs = vgg.input, outputs=prediction)

model.summary()

model.compile(
    loss='categorical_crossentropy',
    optimizer = 'adam',
    metrics=['accuracy']
)

train_data_generator = ImageDataGenerator(rescale=1./255,
                                          shear_range=0.2,
                                          zoom_range=0.2,
                                          horizontal_flip=True)

test_data_generator = ImageDataGenerator(rescale=1./255)

train_dataset = train_data_generator.flow_from_directory('Dataset/train',
                                                         target_size=(224,224),
                                                         batch_size=32,
                                                         class_mode='categorical')
test_dataset = test_data_generator.flow_from_directory('Dataset/test',
                                                       target_size=(224,224),
                                                       batch_size=32,
                                                       class_mode='categorical')

model_vgg16 = model.fit_generator(
    train_dataset,
    validation_data=test_dataset,
    epochs=5,
    steps_per_epoch=len(train_dataset),
    validation_steps=len(test_dataset)
)

# plt.plot(model_vgg16.history['loss'],label='Train loss')
# plt.plot(model_vgg16.history['val_loss'],label='Val loss')
# plt.legend()
# plt.show()
# plt.savefig('LossVal_loss')
print(model_vgg16.history)
plt.plot(model_vgg16.history['accuracy'],label='Train accuracy')
plt.plot(model_vgg16.history['val_accuracy'],label='VAl accuracy')
plt.legend()
plt.show()
plt.savefig('AccVal_acc')

import tensorflow as tf
from keras.models import load_model
model.save('model_vgg16.h5')


