# **Overview**

Once the payload exploits the target system, in our case, a Windows 10 system. It starts to take screenshots in a predefined intervals (link to usage guide) on the compromised computer and save the image to a predefined directory on the compromised computer. It then compares the images and deletes one image if both the images are similar and creates a zip file. Now it checks whether the system has internet connectivity, if yes, then it sends the zip file in the email (change email guide) and then deletes the images along with the zip files and starts fresh again. If the system does not have internet connectivity it continues to take screenshots and checks for the internet connectivity again and so the loop goes on.

# **Technologies**
  * Python 3.6

# **Setup**

The code is written in Python 3.6. If you don't have python installed in your system you can find it [here](https://www.python.org/downloads/). To install the required packages and libraries, run this command in the project directory after cloning the repository.


    pip install -r requirements.txt

# **Features** 
1. Captures screenshots remotely
2. Converts the images to zip file
3. Sends the zip file in E-mail
4. No need to connect to the network
5. Automated Screenshots
6. Deletes the images along with the zip file

# **Use Guide**

First step is to change the email and password in the code as described in below screenshot

![Alt Text](https://github.com/UVvirus/screenshot_grabber/blob/master/Screenshot%20gfrom%202021-01g-20%2009-41-19.png)

After completing the above steps convert the python(py) file to windows executable(EXE) using Pyinstaller
    
    pyinstaller --add-data '<pdf_file_name>.pdf;.' --onefile  --icon="<icon_file_name>.ico --noconsole 'filename.py'




