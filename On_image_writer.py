from Get_prediction import getPrediction
import glob
from PIL import Image, ImageFont, ImageDraw


# this method is need to write a prediction of the image
def write_prediction_on_image(image_path):
    prediction = getPrediction(image_path=image_path)
    definition = prediction[0]
    probability = prediction[1]
    img = Image.open(image_path)
    font = ImageFont.truetype('fonts/calibri.ttf', 28)
    font_1 = ImageFont.truetype('fonts/calibri.ttf', 30)
    draw = ImageDraw.Draw(img)

    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text(xy=(20, 20), text=definition, fill=(0, 0, 0), font=font)
    draw.text(xy=(0, 200), text=str(probability)+'%', fill=(0, 0, 0), font=font_1)
    # img.save('assets/'+image_path)
    img.save('assets/'+image_path[26:])


def proceed_through_all_images():
    images = glob.glob("dataset/single_prediction/*.png")
    for image in images:
        write_prediction_on_image(image_path=image)

