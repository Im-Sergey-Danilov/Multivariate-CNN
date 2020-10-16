
from tensorflow import keras
import numpy as np
from keras.preprocessing import image
from CNN import label_map

model = keras.models.load_model('saved_models/test_saved')


def single_prediction_from_folder(path):
    test_image = image.load_img(path, target_size=(256, 256))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)[0]

    key = ''
    for keys, values in label_map.items():
        if str(values) == str(result.argmax(axis=-1)):
            key = keys
    print("probability of being a class №", key, 'is ' + str(max(result)) + '%')
    print("Количество моточасов = " + str(int(key) * 25))
    return key

# to get a single prediction out of CNN model fill the path variable with (path='path/to/your/file/*.png')
path = 'path/to/your/file/*.png'
print(single_prediction_from_folder(path=path))


