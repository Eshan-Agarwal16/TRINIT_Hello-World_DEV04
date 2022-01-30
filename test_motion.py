import cv2
import numpy as np
from playsound import playsound
from datetime import datetime
import smtplib
import imghdr
from email.message import EmailMessage
from cv2 import subtract
from PIL import Image
import os
import json
import requests

headers = {"Authorization": "Bearer ya29.A0ARrdaM8G3n5cExNSrR8UnC370rDGr6i3fv3idQo10U0UtQcqjQOlJlZ2jeOMRB7Fvi8v_mSJJiJoKYclKx0StOm3YFQlNmJ3PLsYw4imy8AoCd9OoZH-QJc3goWqYeH0xIXW5IEscfUyvumMOuWuQy7Okg5b"}

para = {
    "name": "recording.avi",
}



def save_img(img):
   img_name = "C:\\Users\eshan\OneDrive\Documents\Hello World\Output\Photos"+ now.strftime("\img_%d!%m!%Y_%H!%M!%S") + ".jpg"
   cv2.imwrite(img_name,img)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))

frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter("C:\\Users\eshan\OneDrive\Documents\Hello World\Output\Videos\output.avi", fourcc, 5.0, (1280,720))

ret, frame1 = cap.read()
ret, frame2 = cap.read()
print(frame1.shape)

num = 900000
min15_timer = num
min15_timer_face = num

while cap.isOpened():
    now = datetime.now()
    min15_timer=min15_timer+1
    min15_timer_face=min15_timer_face+1
    diff = cv2.absdiff(frame1, frame2)
    gray_frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray_frame2, 1.2, 7)


    for (x, y, w, h) in faces:
        cv2.rectangle(frame2, (x, y), (x+w, y+h), (255, 0, 0), 2)
        if min15_timer_face>num: 
            min15_timer_face=0

            # Image saving
            im = Image.fromarray(frame2)
            im.save("img.png")

             # email creation
            EMAIL_ADDRESS = 'cctvc0285@gmail.com'
            EMAIL_PASSWORD = 'cctvcctv123'

            contacts = ['cctvc0285@gmail.com']

            msg = EmailMessage()
            msg['Subject'] = 'Detected !!!'
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = contacts
            msg.set_content('Alert!! Suspect face detected!!')
          
            files = []
            files.append('img.png')

            for img in files :
                with open(img,'rb') as f:
                  file_data = f.read()
                  file_type = imghdr.what(f.name)
                  file_name = f.name
                  print(file_name+file_type)
                  msg.add_attachment(file_data, maintype = 'image' , subtype = file_type, filename = file_name)

            # sending email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)

            # removing image
            os.remove('img.png')
        

    if contours:
        image = cv2.resize(frame2, (1280,720))
        cv2.putText(image, now.strftime("%d/%m/%Y  %H:%M:%S"), (int(cap.get(3)) + 150, int(cap.get(4)) + 200), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
        out.write(image)
        if min15_timer>num:
          playsound("C:\\Users\eshan\OneDrive\Documents\Hello World\Assets\chime.wav")
          min15_timer=0

          # email creation
          EMAIL_ADDRESS = 'cctvc0285@gmail.com'
          EMAIL_PASSWORD = 'cctvcctv123'

          contacts = ['cctvc0285@gmail.com']

          msg = EmailMessage()
          msg['Subject'] = 'Alert !!!'
          msg['From'] = EMAIL_ADDRESS
          msg['To'] = contacts
          msg.set_content('Alert!! Suspicious activity!!')

          # sending email
          with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
              smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
              smtp.send_message(msg)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 255), 3)

    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    cv2.imshow("feed", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()
    if min15_timer>10e7:
        min15_timer=num
    if min15_timer_face>10e7:
        min15_timer_face=num
    if cv2.waitKey(40) == 27:
        break

files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open(".\Output\Videos\output.avi", "rb")
}

r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)
out.release()
cap.release()
cv2.destroyAllWindows()