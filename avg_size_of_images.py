from matplotlib import pyplot
from matplotlib.image import imread
# define location of dataset
folder = 'dataset/test_set/defect/'
# plot first few images
for i in range(9):
	# define subplot
	pyplot.subplot(330 + 1 + i)
	# define filename
	filename = folder + 'defect (' + str(181+i) + ').png'
	# load image pixels
	image = imread(filename)
	# plot raw pixel data
	pyplot.imshow(image)
# show the figure
pyplot.show()