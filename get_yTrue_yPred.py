import glob
from single_prediction import single_prediction_from_folder
from math import floor
from dataframe import get_data_of_bearings


def get_yTrue_yPred():
    y_True = []
    y_Pred = []
    for i in range(1, 208):
        images = glob.glob('E:/project/validation_data/'+str(i)+'/*.png')
        print(get_data_of_bearings(class_number=str(i)))
        if get_data_of_bearings(class_number=str(i)) == 100:
            if len(images) > 0:
                for image in images:
                    image_conc = image[27:]
                    image_True = image_conc.split("-", 1)[0]
                    true = image_True[0:floor(len(image_True)/2)]
                    y_Pred.append(single_prediction_from_folder(image))
                    y_True.append(true)
                    print(y_Pred, y_True)
        else:
            pass
    print(y_Pred)
    print(y_True)
    return y_Pred, y_True


get_yTrue_yPred()



