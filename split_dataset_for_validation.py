# todo: split data for validation / take 12 samples from each class
# todo: process all the samples using single prediction
# todo: fill y_true array with startName of image and y_pred array with predictions from CNN

import glob
import os
from PIL import Image

validation_set = glob.glob("E://project/Train_Spektrogramm_8s/*.png")
counter = 0
for each_image in validation_set:
    counter += 1
    if counter % 2 !=0:
        image_valid = each_image[34:]
        image_validation = image_valid.split("-", 1)[0]

        if not os.path.exists("E://project/validation_data/"+image_validation):
            os.makedirs("E://project/validation_data/"+image_validation)
        img = Image.open("E://project/Train_Spektrogramm_8s/"+image_valid)
        if len(glob.glob("E://project/validation_data/"+image_validation+"/*.png")) < 12:
            img.save("E://project/validation_data/"+image_validation+"/"+image_valid)

