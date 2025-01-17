# import cv2, numpy as np

# img = np.ones((100,100))*100

# while True:
#     cv2.imshow('tracking',img)
#     keyboard = cv2.waitKey(1)   & 0xFF
#     if keyboard !=255:
#         print keyboard
#     if keyboard==27 or keyboard==ord('q'):
#         break
# cv2.destroyAllWindows()

#!/usr/bin/env python

import numpy as np
import cv2
import os
import v4l2capture
import select
import time

# Open the video device.
video = v4l2capture.Video_device("/dev/video0")

# Suggest an image size to the device. The device may choose and
# return another size if it doesn't support the suggested one.
size_x, size_y = video.set_format(1920, 1080)

print "device chose {0}x{1} res".format(size_x, size_y)

# Create a buffer to store image data in. This must be done before
# calling 'start' if v4l2capture is compiled with libv4l2. Otherwise
# raises IOError.
video.create_buffers(30)

# Send the buffer to the device. Some devices require this to be done
# before calling 'start'.
video.queue_all_buffers()

# Start the device. This lights the LED if it's a camera that has one.
print "start capture"
video.start()

while(True):
    #We used to do the following, but it doesn't work :(
    #ret, frame = cap.read()
    
    #Instead...
    
    # Wait for the device to fill the buffer.
    select.select((video,), (), ())

    # The rest is easy :-)
    image_data = video.read_and_queue()
    
    print "decode"
    frame = cv2.imdecode(np.frombuffer(image_data, dtype=np.uint8), cv2.cv.CV_LOAD_IMAGE_COLOR)


    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

#cap.release()
video.close()

cv2.destroyAllWindows()