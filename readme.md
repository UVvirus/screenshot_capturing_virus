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



# **License**

copyrights © 2021 UVvirus 

Permission is hereby granted, free of charge, to any person obtaining a copy of this code, to deal in the code without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, subjected to the following conditions:
* The above copyright notice and this permission notice shall be included in all copies or substantial portion of the software.
* Must follow all the code of ethics for ethical hacking.

