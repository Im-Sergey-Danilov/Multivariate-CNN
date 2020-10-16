from PIL import Image

img = Image.new("RGB", (300, 100), "white")
lay1 = Image.new("RGB", (300, 100), "blue")
lay2 = Image.new("RGB", (300, 100), "red")
img.paste(lay1, (100, 0))
img.show()
