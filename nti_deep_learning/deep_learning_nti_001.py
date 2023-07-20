# -*- coding: utf-8 -*-
"""deep_learning_nti_001

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TDvSsYVIcVfR06rhdYRc1DDbvtXGh_em
"""

import tensorflow as tf

from keras.models import Sequential
from keras.layers import Dense
import numpy

numpy.random.seed(7)

import pandas as pd
df= pd.read_csv('diabetes3.csv')
x=df.iloc[:,0:8].values
y=df.iloc[:,8].values

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.30,random_state=0)
x.shape

#create mode
model= Sequential()
model.add(Dense(12,input_dim=8,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(1,activation='relu'))

#compile
model.compile(loss='binary_crossentropy',optimizer='adam',metrics='accuracy')

#before imputting

history=model.fit(x_train,y_train,epochs=150,batch_size=10)

#evaluate the model
scores = model.evaluate(x_test,y_test)

pip install ann_visualizer

pip install graphviz

from graphviz import Digraph

from ann_visualizer.visualize import ann_viz

#visualizing
from  ann_visualizer.visualize import ann_viz
ann_viz(model, title="neural network",filename='test.gv')

import matplotlib.pyplot as plt

loss = history.history['loss']

# Plot the accuracy
plt.plot(loss, 'g', label='Training loss')
plt.title('Training Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

accuracy = history.history['accuracy']

# Plot the accuracy
plt.plot(accuracy, 'g', label='Training Accuracy')
plt.title('Training Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim(0.6, 1)
plt.legend()
plt.show()

import numpy as np

# fitting after imputting
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=0,strategy="mean")
imputer=imputer.fit(x[:,1:7])
x[:,1:7]=imputer.transform(x[:,1:7])

x=pd.DataFrame(x)
print(x.head())

#create mode
model1= Sequential()
model1.add(Dense(12,input_dim=8,activation='relu'))
model1.add(Dense(8,activation='relu'))
model1.add(Dense(1,activation='relu'))

#compile
model1.compile(loss='binary_crossentropy',optimizer='adam',metrics='accuracy')

x_train1,x_test1,y_train1,y_test1=train_test_split(x,y,test_size=.30,random_state=0)
history1=model1.fit(x_train1,y_train1,epochs=150,batch_size=10)