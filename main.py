from PIL import ImageGrab
import os
import random

rand=random.randint(10000,300000)

def take_screenshot():
    image= ImageGrab.grab()
    path='/home/sk84/PycharmProjects/scrrenshot_project/pics'
    try:
        os.mkdir(path)
        image.save('/home/sk84/PycharmProjects/scrrenshot_project/pics/test'+str(rand)+'.jpg')
    except OSError:
        if os.path.exists(path):
            image.save('/home/sk84/PycharmProjects/scrrenshot_project/pics/test' + str(rand) + '.jpg')


if __name__ == '__main__':
    take_screenshot()


