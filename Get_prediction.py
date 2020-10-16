import numpy as np
from keras.preprocessing import image

from tensorflow import keras

from keras.preprocessing.image import ImageDataGenerator


def getPrediction(image_path):
    train_datagen = ImageDataGenerator(
        rescale=1.,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
    training_set = train_datagen.flow_from_directory(
        'dataset/training_set',
        target_size=(256, 256),
        batch_size=32,
        class_mode='binary')

    model = keras.models.load_model('saved_models')
    # Load the image & path to image we should process
    test_image = image.load_img(image_path, target_size=(256, 256))
    # Change to a 3 Dimensional array because it is a colour image
    test_image = image.img_to_array(test_image)
    # add a forth dimension
    test_image = np.expand_dims(test_image, axis=0)

    print('HERE')
    result = model.predict(test_image)
    training_set.class_indices
    # threshold of 50% to classify the image
    if result[0][0] > 0.5:
        prediction = 'Non-Defect'
    else:
        prediction = 'Defect'
        result[0][0] = 1 - result[0][0]

    print(result[0][0], "% certainty of being", prediction)
    return prediction, result[0][0]


print(getPrediction(image_path="dataset/single_prediction/defect_1.png"))

