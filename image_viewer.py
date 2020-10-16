from tkinter import *
import glob
from PIL import Image, ImageTk
from On_image_writer import proceed_through_all_images



root = Tk()
root.title('CNN performance on Spectrogram')
proceed_through_all_images()
images = glob.glob("assets/*.png")
image_list = []
for image in images:
    img = ImageTk.PhotoImage(Image.open(image))
    image_list.append(img)

label = Label(image=image_list[0])


def forward(image_number):
    global label
    global button_forward
    global button_back
    label.grid_forget()
    label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number+1))
    button_back = Button(root, text='<<', command=lambda: back(image_number-1))
    if image_number == len(image_list):
        button_forward = Button(root, text=">>", state=DISABLED)
    label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(image_number):
    global label
    global button_forward
    global button_back

    label.grid_forget()
    label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number + 1))
    button_back = Button(root, text='<<', command=lambda: back(image_number - 1))
    if image_number == 0:
        button_forward = Button(root, text=">>", state=DISABLED)
    label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="X", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
root.mainloop()
