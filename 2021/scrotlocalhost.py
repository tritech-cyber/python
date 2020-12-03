#!/usr/bin/env python3 
# cwc  - upload to python repo in github.com
import os
print("This python code will ask for an image file name ")
print("then add a file type of .png.")
print("The *.png will be saved in the directory where this python file is executed.")
imagename = input("Imput a name for an image : ")
oscommand = "scrot "+imagename+".png"
print(oscommand)
#os.system('sleep 5')
os.system(oscommand)

'''
If the "scrot screebshot.png" command is typed in terminal it will capture the screen.

Now the challenge is to pause 5 secords then hide terminal using os.system('sleep 5')
'''
