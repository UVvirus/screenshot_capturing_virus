from PIL import ImageGrab
import time
import os
import uuid
path = '/home/sk84/PycharmProjects/scrrenshot_project/pics/'


def take_screenshot():
    """""
    This method will take screenshot and save it in a "pics" folder
    """""

    global index, images

    i=uuid.uuid4()
    index=i.int
    try:

        os.mkdir(path)

        while True:

                print("loop is running")
                images = ImageGrab.grab()
                images.save('/home/sk84/PycharmProjects/scrrenshot_project/pics/' + str(index)+'.jpg' )
                index = index + 1
                time.sleep(2)

    except OSError:
        while True:
         if os.path.exists(path):
             images = ImageGrab.grab()
             images.save('/home/sk84/PycharmProjects/scrrenshot_project/pics/' + str(index) + '.jpg')
             index = index + 2
             print(index)
             time.sleep(2)


if __name__ == '__main__':
    take_screenshot()


