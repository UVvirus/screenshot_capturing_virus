from PIL import ImageGrab,ImageSequence,Image
import os
import time





path = '/home/sk84/PycharmProjects/scrrenshot_project/pics'
global index

def take_screenshot():
    """""
    This method will take screenshot and save it in a "pics" folder
    """""
    index=1

    try:

        os.mkdir(path)
        while True:
            print("loop starts")
            images = ImageGrab.grab()
            print(images)
            print("grabbed")
            #for image in ImageSequence.Iterator(images):
            images.save('/home/sk84/PycharmProjects/scrrenshot_project/pics/test' + str(index) + '.jpg')
            index=index+1
            print(index)
            print("saved")
            time.sleep(2)
            print("sleeping 2 secs")

    except OSError:
        if os.path.exists(path):
            images.save('/home/sk84/PycharmProjects/scrrenshot_project/pics/test' + str(index) + '.jpg')


if __name__ == '__main__':
    take_screenshot()


