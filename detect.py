import datetime
from tensorflow.keras.models import load_model
from matplotlib import pyplot as plt
from create_unet import create_model
import numpy as np
import cv2
import os
def import_network(file):
    model = load_model(file)
    return model
def resize_photo(image, shapes=(256, 256)):
    resized_photo = cv2.resize(image, shapes)
    return resized_photo
def import_weights_of_network(file):
    model = create_model()
    model.load_weights('model.h5')
    return model
def load_photo(file):
    image = cv2.imread(file)
    resized_photo = resize_photo(image)
    return np.array([resized_photo]), image.shape
def reverse(model, image):
    mask = model.predict(image, verbose=0)
    return mask
def recoding(mask):
    mask = mask[0]
    mask2 = np.zeros((256, 256, 1))
    for x in range(256):
        for y in range(256):
            pixel = mask[x, y]
            if pixel[0]>pixel[1]:
                mask2[x, y] = 0
            else:
                mask2[x, y] = 250
    return mask2
def show_mask(mask):
    plt.imshow(mask)
    plt.show()
def find_images():
    files = os.listdir(r'.')
    images = []
    for file in files:
        if file.endswith('.jpg') or file.endswith('.png'):
            images.append(file)
    if len(images) > 1:

        print('Напишите название файла, который хотите использовать, вот их список')
        print(images)
        image = input()
    else:
        image = images[0]
    return image
def save_image(num, image, original_image):
    image = image.tolist()
    original_image = original_image.tolist()
    for row_ind in range(len(image)):
        image[row_ind] = [[pixel, 0, 0] for pixel in image[row_ind]]
        image[row_ind] = image[row_ind]+original_image[row_ind]
    image = np.array(image)
    cv2.imwrite('images/'+str(num)+'.jpg', image)

def detect_human(model, camera):
    date = str(datetime.datetime.now())
    #print('Вы хотите испоьлзовать локальный путь? Нажмите Enter, если да, или введите "n", если нет')
    r'''image_file = input()
    if not image_file:
       image_file = find_images()'''


    ret, image_original = camera.read()
    image_shape = image_original.shape
    image = resize_photo(image_original)
    image = np.array([image])
    mask = reverse(model, image)
    mask2 = recoding(mask)

    mask2 = np.array(mask2, dtype=np.uint8)
    if mask2.sum()/mask2.size/250>=0.1:
        #print(mask2.sum()/mask2.size, mask2.sum(), mask2.size, mask2.max())
        mask2 = resize_photo(mask2, image_shape[:-1][::-1])
        save_image(date, mask2, image_original)
        return True, date
    else:
        return False, date



