import tensorflow as tf
from keras.datasets import fashion_mnist
from keras.layers import Conv2D, Flatten, Dense
import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt
from keras.models import Sequential
from sklearn.metrics import accuracy_score
nc = 10 # Number of classes

#This is a dataset of 60,000 28x28 grayscale images of 10 fashion categories, 
#along with a test set of 10,000 images. This dataset can be used as a drop-in 
#replacement for MNIST.
# Label	Description
# 0	T-shirt/top
# 1	Trouser
# 2	Pullover
# 3	Dress
# 4	Coat
# 5	Sandal
# 6	Shirt
# 7	Sneaker
# 8	Bag
# 9	Ankle boot

(Xtrain, ytrain), (Xtest, ytest) = fashion_mnist.load_data()

#Show sample images
plt.figure(1)
imgplot1 = plt.imshow(Xtrain[nr.randint(60000)])
plt.show()

plt.figure(2)
imgplot2 = plt.imshow(Xtrain[nr.randint(60000)])
plt.show()

Xtrain = Xtrain.reshape(60000,28,28,1)
Xtest = Xtest.reshape(10000,28,28,1)

ytrainEnc = tf.one_hot(ytrain, depth=nc)
ytestEnc = tf.one_hot(ytest, depth=nc)


model=Sequential()
model.add(Conv2D(64,kernel_size=3, activation="relu",input_shape=(28,28,11)))
model.add(Conv2D(32,Kernel_size=3, activation="relu"))
model.add(Flatten())
model.add(Dense(10,activation="softmax"))
model.compile(lose='catagorical_crossentropy',optimizer='adam',matrics=['accuracy'])

model.fit(Xtrain,ytrainEnc,validation_data=(Xtest,ytestEnc),epochs=3)

ypred = model.predict(Xtest)
ypred = np.argmax(ypred,axis=1)

score = accuracy_score(ypred,ytest)
print('Accuracy score is',100*score,'%')

