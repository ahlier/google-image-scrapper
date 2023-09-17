from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from auto_screenshot import *
import os
def del_white_row(matrix):  # this will return rows with images
    image_row = []
    for i in range(len(matrix)):
        # white row will have length 1, and images have large length.
        if matrix[i].shape[0] > 50:
            image_row.append(i)

    return [matrix[i] for i in image_row]

def del_white_column(matrix):   # this will return columns with images
    image_column = []
    for i in range(len(matrix)):
        if matrix[i].shape[1] > 50:
            image_column.append(i)

    return [matrix[i] for i in image_column]


def crop(file):
    path = 'C:/python file/project/identifier/pictures/{}/'.format(file)
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
        print('new directory is created')

    image = Image.open('{}.png'.format(file))
    np_image = np.array(image)

    image_rightcropped = list(map(lambda x: x[:1040], np_image))
    # convert array into list, we cannot delete column on an array directly is because the size of each row need to be the
    # same for array.
    # lambda will take the first 1040 elements, which will get rid of the bar at the right edge.
    # map() will pass all elements in np_image (all the row) to this lambda function.

    indices = []  # this records the indices of white rows
    last = image_rightcropped[0]
    for i in range(len(image_rightcropped)):  # for loop will run through the rows
        if (image_rightcropped[i] == last).all():  # it checks if all elements in this row are the same as the last row
            # If these two rows are the same, then they are white.
            indices.append(i)
        last = image_rightcropped[i]

    horizontal_split = np.split(image_rightcropped, indices)
    # the row with images will have large len, but the white row will have only 1 len

    horizontal_split = del_white_row(horizontal_split)[3:]
    images = []

    for row in horizontal_split:
        row_indices = []
        last = row[:, 0]
        for i in range(row.shape[1]):
            if (row[:, i] == last).all():
                row_indices.append(i)
            last = row[:, i]
        vertical_split = np.split(row, row_indices, 1)
        images.extend(del_white_column(vertical_split))

    for i in range(len(images) - 2):
        img = plt.imshow(images[i])
        plt.xticks([])
        plt.yticks([])
        plt.savefig('{}{}.jpg'.format(path, i))

search = 'cute anime girl'  # string that will be put to google search
screenshot('cute anime girl')   # this will create a long screenshot of search item
crop(search)    # this will crop the long screenshot into many small individual images