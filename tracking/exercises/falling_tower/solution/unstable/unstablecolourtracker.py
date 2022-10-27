# ----------------------- importing necessary packages ----------------------- #
from optparse import Values
import cv2
import numpy as np
from matplotlib import pyplot as plt

# ---------------------------- importing the video --------------------------- #
imported_video = cv2.VideoCapture("UnstableVideo.mp4")

# -------------------------- getting video metadata -------------------------- #
frame_width = int(imported_video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(imported_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
number_of_frames = int(imported_video.get(cv2.CAP_PROP_FRAME_COUNT))
print(number_of_frames)

slow_motion_factor = 1/32
fps = imported_video.get(cv2.CAP_PROP_FPS) / slow_motion_factor

# -------------------- defining hsv lower and upper bounds ------------------- #
green_lower_bound = np.array([40, 170, 20])
green_upper_bound = np.array([75, 250, 255])

purple_lower_bound = np.array([125, 50, 20])
purple_upper_bound = np.array([140, 200, 255])

# ------------------ initializing coordinate and time lists ------------------ #
green_x_list = []
green_t_list = []

purple_y_list = []
purple_t_list = []

# ---------- iterating over frames and getting position of the block --------- #
for index in range(number_of_frames):
    was_successful, frame = imported_video.read()
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # ------------------------------ green block ----------------------------- #

    green_mask_frame = cv2.inRange(hsv_frame, green_lower_bound, green_upper_bound)

    green_contours, hierarchy = cv2.findContours(green_mask_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in green_contours:
        if cv2.contourArea(contour) > 1000:
            x, y, width, height = cv2.boundingRect(contour)
            green_x_list.append(x + width/2)
            green_t_list.append(index * 1.0 / fps)
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 3)

    # ------------------------------ purple block ---------------------------- #

    purple_mask_frame = cv2.inRange(hsv_frame, purple_lower_bound, purple_upper_bound)

    purple_contours, hierarchy = cv2.findContours(purple_mask_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in purple_contours:
        if cv2.contourArea(contour) > 1000:
            x, y, width, height = cv2.boundingRect(contour)
            purple_y_list.append(y + height/2)
            purple_t_list.append(index * 1.0 / fps)
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 3)

    cv2.imshow("frame", frame)

    cv2.waitKey(1)

# ------------------------ creating arrays from lists ------------------------ #

green_x_array = np.array(green_x_list)
green_t_array = np.array(green_t_list)

purple_y_array = np.array(purple_y_list)
purple_t_array = np.array(purple_t_list)

# -------------------- transforming the pixel coordinates -------------------- #
pixel_to_meter = 0.00018
green_x_array = pixel_to_meter * green_x_array
purple_y_array = pixel_to_meter * (frame_height - purple_y_array)

# --------------------------- plotting the results --------------------------- #

fig1, ax1 = plt.subplots(dpi = 200)
ax1.plot(green_t_array, green_x_array)
ax1.set(xlabel = "Time (s)", ylabel = "x (m)")
ax1.set_title("Bottom Block x-Position")
ax1.grid()

fig2, ax2 = plt.subplots(dpi = 200)
ax2.plot(purple_t_array, purple_y_array)
ax2.set(xlabel = "Time (s)", ylabel = "y (m)")
ax2.set_title("Top Block y-Position")
ax2.grid()

fig1.savefig("greenresult.png")
fig2.savefig("purpleresult.png")