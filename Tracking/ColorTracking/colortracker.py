# ----------------------- importing necessary packages ----------------------- #
import cv2
import numpy as np
from matplotlib import pyplot as plt

# ---------------------------- importing the video --------------------------- #
importedVideo = cv2.VideoCapture("video.mp4")

# -------------------------- getting video metadata -------------------------- #
widthOfFrame = int(importedVideo.get(cv2.CAP_PROP_FRAME_WIDTH))
heightOfFrame = int(importedVideo.get(cv2.CAP_PROP_FRAME_HEIGHT))
numberOfFrames = int(importedVideo.get(cv2.CAP_PROP_FRAME_COUNT))
fps = importedVideo.get(cv2.CAP_PROP_FPS)

# -------------------- defining hsv lower and upper bounds ------------------- #
lowerBound = np.array([85, 170, 110])
upperBound = np.array([115, 250, 255])

# ------------------ initializing coordinate and time array ------------------ #
xArray = np.zeros(numberOfFrames)
yArray = np.zeros(numberOfFrames)
tArray = np.zeros(numberOfFrames)

# ---------- iterating over frames and getting position of the cart ---------- #
for index in range(numberOfFrames):
    wasSuccessful, frame = importedVideo.read()

    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    maskFrame = cv2.inRange(hsvFrame, lowerBound, upperBound)

    contours, hierarchy = cv2.findContours(maskFrame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 1000:
            x, y, width, height = cv2.boundingRect(contour)
            xArray[index] = x + width/2
            yArray[index] = y + height/2
            tArray[index] = index * 1.0 / fps

# -------------------- transforming the pixel coordinates -------------------- #
pixelToMeter = 0.0001
xArray = pixelToMeter * xArray
yArray = pixelToMeter * (heightOfFrame - yArray)

# --------------------------- plotting the results --------------------------- #
fig, (firstFigure, secondFigure) = plt.subplots(2, 1)
firstFigure.plot(tArray, xArray, color = "blue")
firstFigure.set(ylabel = "x (m)")
firstFigure.grid()

secondFigure.plot(tArray, yArray, color = "blue")
secondFigure.set(xlabel = "Time (s)", ylabel = "y (m)")
secondFigure.grid()

fig.savefig("result.png")