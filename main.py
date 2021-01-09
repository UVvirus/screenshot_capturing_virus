from PIL import ImageGrab
import time
import os
import uuid
import dhash
from PIL import Image
import imagehash

path = '/home/sk84/PycharmProjects/scrrenshot_project/pics'


def d_hash(image1, image2):
    print("inside dhash ")
    row1, col1 = dhash.dhash_row_col(image1)
    row2, col2 = dhash.dhash_row_col(image2)

    hash1 = dhash.format_hex(row1, col2)
    hash2 = dhash.format_hex(row2, col2)

    if hash1 == hash2:
        print("inside dhash if")
        path1 = path + '/' + str(index) + '.jpg'
        os.remove(path1)


def take_screenshot():
    """""
    This method will take screenshot and save it in a "pics" folder
    """""

    global index, images, i, j
    images_list = []
    id = uuid.uuid4()
    index = id.int

    try:
        i = 0

        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
            print("before 1st while")
        while True:

            print("loop is running")
            j = i - 1
            images = ImageGrab.grab()
            images_list.append(images)
            print(images_list)
            images.save(path + '/' + str(index) + '.jpg')

            if i > 0:
                d_hash(images_list[i], images_list[j])
                print("remaining list:", images_list)

            index = index + 1
            i += 1
            # print("i value after func call:", images_list[i])
            print("j value after func call:", images_list[j])
            print("==============================================================================================")
            time.sleep(3)

    except OSError:
        print("error")
        take_screenshot()


if __name__ == '__main__':
    take_screenshot()



