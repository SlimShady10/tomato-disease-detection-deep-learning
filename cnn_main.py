# -*- coding: utf-8 -*-
"""CNN.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12Dts86_KC_iLe1Qp55oK_FFUBD5LaWvm
"""

from google.colab import drive
drive.mount('/content/drive')

import os
import numpy as np
import pandas as pd
import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Activation, Dropout, Flatten, Dense,Input
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D,Conv2D
from keras import optimizers
from keras import applications
from keras.models import Model
from keras import models
import keras.backend as K
from keras.layers import BatchNormalization
from tensorflow import keras
from keras import regularizers
from tensorflow.keras.preprocessing.image import img_to_array,load_img
from keras.callbacks import EarlyStopping

img_width, img_height = 109, 109

AUTOTUNE = tf.data.experimental.AUTOTUNE

#!pip install split-folders

#import splitfolders
#input_folder= "/kaggle/input/akishore1/AD8"
# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
#splitfolders.ratio(input_folder, output="output_AD1", seed=1337, ratio=(.7, .1, .2)) #default values

train_data_dir = '/content/drive/MyDrive/Plant_Leaf_Disease_Dataset/train'
validation_data_dir = '/content/drive/MyDrive/Plant_Leaf_Disease_Dataset/valid'

train_datagen = ImageDataGenerator(rescale=1./255, horizontal_flip=True)
validation_datagen = ImageDataGenerator(rescale=1./255)
batch_size = 32

train_generator  = train_datagen.flow_from_directory(train_data_dir,
                                                     target_size=(img_width, img_height),
                                                   color_mode='grayscale',
                                                   shuffle='True',
                                                    batch_size=32,
                                                   class_mode='categorical',seed=42)

validation_generator = validation_datagen.flow_from_directory(directory = validation_data_dir,
                                                   target_size=(img_width, img_height),color_mode='grayscale',
                                                   batch_size=32,
                                                   class_mode='categorical',seed=42)

def f1_score(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    recall = true_positives / (possible_positives + K.epsilon())
    f1_val = 2*(precision*recall)/(precision+recall+K.epsilon())
    return f1_val

model = Sequential()

model.add(Convolution2D(32, (3, 3), input_shape=(img_width, img_height,1)))
model.add(Activation('relu'))

model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())
model.add(Convolution2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())
model.add(Convolution2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())
model.add(Convolution2D(128, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())
model.add(Flatten())
model.add(BatchNormalization())
model.add(Dense(256,kernel_regularizer=keras.regularizers.l2(0.01)))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(BatchNormalization())
model.add(Dense(10))
model.add(Activation('softmax'))

model.summary()

METRICS = [
      tf.keras.metrics.BinaryAccuracy(name='accuracy'),
      tf.keras.metrics.Precision(name='precision'),
      tf.keras.metrics.Recall(name='recall'),
      tf.keras.metrics.AUC(name='auc'),
      f1_score,
]

model.compile(loss='categorical_crossentropy',
              optimizer='nadam',
              metrics=METRICS)

callbacks = EarlyStopping(monitor='val_loss',
    min_delta=0.00001,
    patience=20,
    verbose=1,
    mode='auto',
    baseline=None,
    restore_best_weights=False)

from keras.callbacks import ModelCheckpoint
checkpointer=ModelCheckpoint("my_files.hd5",monitor='val_accuracy',mode='max',save_best_only=True,verbose=1)
epochs =30

history=model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // train_generator.batch_size,
        epochs=epochs,
        callbacks=callbacks,
        validation_data=validation_generator,
        validation_steps=validation_generator.samples//validation_generator.batch_size)

scores = model.evaluate(validation_generator)
print("Accuracy = ", scores[1])
print("Precision = ", scores[2])
print("Recall = ", scores[3])
print("AUC = ", scores[4])
print("F1_score = ", scores[5])

#%% PLOTTING RESULTS (Train vs Validation FOLDER 1)

import matplotlib.pyplot as plt
def Train_Val_Plot(acc,val_acc,loss,val_loss,auc,val_auc,precision,val_precision,f1,val_f1):

    fig, (ax1, ax2,ax3,ax4,ax5) = plt.subplots(1,5, figsize= (25,4))
    fig.suptitle(" MODEL EVALUATION METRICS CNN")

    ax1.plot(range(1, len(acc) + 1), acc)
    ax1.plot(range(1, len(val_acc) + 1), val_acc)

    ax1.set_xlabel('Epochs')
    ax1.set_ylabel('Accuracy')
    ax1.legend(['training', 'validation'])



    ax2.plot(range(1, len(loss) + 1), loss)
    ax2.plot(range(1, len(val_loss) + 1), val_loss)

    ax2.set_xlabel('Epochs')


    ax2.set_ylabel('Loss')
    ax2.legend(['training', 'validation'])


    ax3.plot(range(1, len(auc) + 1), auc)
    ax3.plot(range(1, len(val_auc) + 1), val_auc)

    ax3.set_xlabel('Epochs')


    ax3.set_ylabel('AUC')
    ax3.legend(['training', 'validation'])

    ax4.plot(range(1, len(precision) + 1), precision)
    ax4.plot(range(1, len(val_precision) + 1), val_precision)

    ax4.set_xlabel('Epochs')

    ax4.set_ylabel('Precision')
    ax4.legend(['training', 'validation'])


    ax5.plot(range(1, len(f1) + 1), f1)
    ax5.plot(range(1, len(val_f1) + 1), val_f1)

    ax5.set_xlabel('Epochs')

    ax5.set_ylabel('F1 score')
    ax5.legend(['training', 'validation'])



    plt.show()



Train_Val_Plot(history.history['accuracy'],history.history['val_accuracy'],
               history.history['loss'],  history.history['val_loss'],   history.history['auc'],  history.history['val_auc'],
               history.history['precision'],history.history['val_precision'],
               history.history['f1_score'],history.history['val_f1_score']
              )