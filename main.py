# Face detection using OpenCV
# Load image from directory or use webcam to capture image

import cv2
from tkinter import Tk, Button, filedialog


def create_button(window, label, loc, fnc):
    assert type(label) == str
    assert type(loc) == tuple and len(loc) == 2
    btn = Button(window, text=label, width=15, command=fnc)
    btn.place(x=loc[0], y=loc[1])
    return btn


def detect_face(img):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Detecting faces from webcam', img)


def from_file():
    file = filedialog.askopenfile()
    img = cv2.imread(file.name)
    detect_face(img)


def from_webcam():
    video_capture = cv2.VideoCapture(0)
    while True:
        ret, frame = video_capture.read()
        k = cv2.waitKey(1)
        detect_face(frame)
        if k % 256 == 27:  # ESC Pressed
            break
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    root.title("Face Detection")
    root.geometry("600x300")
    create_button(root, "From file", (100, 100), from_file)
    create_button(root, "From webcam", (380, 100), from_webcam)
    create_button(root, "Close", (240, 200), root.destroy)
    root.mainloop()





