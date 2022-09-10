# ----------------------- importing necessary packages ----------------------- #
import cv2
import numpy as np
from matplotlib import pyplot as plt

# ---------------------------- importing the video --------------------------- #
imported_video = cv2.VideoCapture("video.mp4")

# -------------------------- getting video metadata -------------------------- #
frame_width = int(imported_video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(imported_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
number_of_frames = int(imported_video.get(cv2.CAP_PROP_FRAME_COUNT))
print(number_of_frames)
fps = imported_video.get(cv2.CAP_PROP_FPS)

# -------------------- defining hsv lower and upper bounds ------------------- #
lower_bound = np.array([85, 170, 110])
upper_bound = np.array([115, 250, 255])

# ------------------ initializing coordinate and time array ------------------ #
x_array = np.zeros(number_of_frames)
y_array = np.zeros(number_of_frames)
t_array = np.zeros(number_of_frames)

# ---------- iterating over frames and getting position of the cart ---------- #
for index in range(number_of_frames):
    was_successful, frame = imported_video.read()

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask_frame = cv2.inRange(hsv_frame, lower_bound, upper_bound)

    contours, hierarchy = cv2.findContours(mask_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 1000:
            x, y, width, height = cv2.boundingRect(contour)
            x_array[index] = x + width/2
            y_array[index] = y + height/2
            t_array[index] = index * 1.0 / fps
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 3)

    cv2.imshow("mask", mask_frame)
    cv2.imshow("frame", frame)

    cv2.waitKey(1)

# -------------------- transforming the pixel coordinates -------------------- #
pixel_to_meter = 0.002
x_array = pixel_to_meter * x_array
y_array = pixel_to_meter * (frame_height - y_array)

# --------------------------- plotting the results --------------------------- #
fig, (first_fig, second_fig) = plt.subplots(2, 1)
first_fig.plot(t_array, x_array)
first_fig.set(ylabel = "x (m)")
first_fig.grid()

second_fig.plot(t_array, y_array)
second_fig.set(xlabel = "Time (s)", ylabel = "y (m)")
second_fig.grid()

fig.savefig("result.png")