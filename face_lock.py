#!/usr/bin/env python3
import face_recognition
from subprocess import call
import os
import time
import subprocess
    
# while True:
# # time.sleep(30)
my_faces = []
for x in os.listdir('/home/ravi/sun/face/me/'):
    picture_of_me = face_recognition.load_image_file("/home/ravi/sun/face/me/"+x)
    try:
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
        my_faces.append(my_face_encoding)
    except IndexError:
        print("No face found"+x)
        pass    

try:
    # take picture of laptop user
    call(["fswebcam", "/home/ravi/sun/face/now.jpg"])
    unknown_picture = face_recognition.load_image_file("/home/ravi/sun/face/now.jpg")
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
    results = face_recognition.compare_faces(my_faces, unknown_face_encoding)

    if any(results) == True:
        print("got my face don't lock")
    else:
        print("faces not matching lock the screen")
        subprocess.Popen(["gnome-screensaver-command", "-l"], env=dict(os.environ, DISPLAY=":0.0", XAUTHORITY="/home/ravi/.Xauthority"))
        
        # call(["gnome-screensaver-command", "-l"])
except IndexError:
    print("IndexError: No faces found lock the screen")
    subprocess.Popen(["gnome-screensaver-command", "-l"], env=dict(os.environ, DISPLAY=":0.0", XAUTHORITY="/home/ravi/.Xauthority"))
    # call(["gnome-screensaver-command", "-l"])
