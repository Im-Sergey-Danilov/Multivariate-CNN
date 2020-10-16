# Convolutional Neural Network

# Written by: Sergey Danilov
# AMM student?
# 16-08-20
# This neural network is trained to differentiate the features
# between defect and non-defect bearings. To test, add an image of a defect or a non-defect to the
# single prediction folder and execute the entire code (besides the fit generator function)


# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

from keras.preprocessing.image import ImageDataGenerator

import numpy as np
from keras.preprocessing import image

from tensorflow import keras

# Initialise the CNN
classifier = Sequential()

# 1 - Build the convolution

# 32 filters or a 3x3 grid
classifier.add(Convolution2D(32, 3, 3, input_shape=(256, 256, 3), activation='relu'))

# 2 - Pooling
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Second layer
classifier.add(Convolution2D(32, 3, 3, activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# 3 - Flattening
classifier.add(Flatten())

# 4 - Full Connection, making an ANN

classifier.add(Dense(units=124, activation='relu'))
# outputdim=168
# multi-outcome so softmax is being used
classifier.add(Dense(units=168, activation='softmax'))

# Compiling the NN

classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Fitting the neural network for the images


train_datagen = ImageDataGenerator(
    rescale=1.,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1.)

training_set = train_datagen.flow_from_directory(
    'dataset/training_set',
    target_size=(256, 256),
    batch_size=32,
    class_mode='categorical')

# easy access to each class further
label_map = training_set.class_indices

test_set = test_datagen.flow_from_directory(
    'dataset/test_set',
    target_size=(256, 256),
    batch_size=32,
    class_mode='categorical')


##### EXECUTE THIS TO TRAIN MODEL ##############
# classifier.fit_generator(
#                 training_set,
#                 epochs=100,
#                 validation_data=test_set,
#                 validation_steps=10
# )
#
# # saving the model
# classifier.save('saved_models/test_saved')
# # --------- New Prediction -------------
#
# # # # Execute to make a single prediction from a saved CNN model # # # #
# model = keras.models.load_model('saved_models/test_saved')
# # Load the image (path to single prediction file
# test_image = image.load_img("E://project/Train_Spektrogramm_8s/1-975.png", target_size=(256, 256))
# # Change to a 3 Dimensional array because it is a colored image
# test_image = image.img_to_array(test_image)
# # add a forth dimension
# test_image = np.expand_dims(test_image, axis=0)
#
#
# result = model.predict(test_image)[0]
#
# # find a class name of prediction
# key = ''
# for keys, values in label_map.items():
#     if str(values) == str(result.argmax(axis=-1)):
#         key = keys
#
#
# print("probability of being a class №", key, 'is '+str(max(result))+'%')
# print("Количество моточасов = "+str(int(key)*25))
# counter = 0

# get the layers of ANN (You must `pip install pydot` and 'pip install graphviz')
# classifier.summary()

# from sklearn.metrics import classification_report, confusion_matrix

# Y_pred = classifier.predict_generator(test_set, 168 // 33)
# y_pred = np.argmax(Y_pred, axis=1)
# # print(Y_pred)
# print('Confusion Matrix')
# print(confusion_matrix(test_set.classes, y_pred))
# print('Classification Report')
# target_names = []
# for i in range(1, 168):
#     target_names.append(str(i))
# print(target_names)
# print(classification_report(test_set.classes, y_pred, target_names=target_names))

# matrix = confusion_matrix(y_pred.argmax(axis=1), result.argmax(axis=1))
# print(matrix)
# print("Вероятность принадлежности к классу", key, "равна "+str(max(result))+"%")
# print('Отработанные моточасы - ' + str(int(key)*25)+" часов")
