# MIT License
# Copyright (c) 2019-2022 JetsonHacks

# Using a CSI camera (such as the Raspberry Pi Version 2) connected to a
# NVIDIA Jetson Nano Developer Kit using OpenCV
# Drivers for the camera and OpenCV are included in the base image

import cv2
import torch
import numpy as np


""" 
gstreamer_pipeline returns a GStreamer pipeline for capturing from the CSI camera
Flip the image by setting the flip_method (most common values: 0 and 2)
display_width and display_height determine the size of each camera pane in the window on the screen
Default 1920x1080 displayd in a 1/4 size window
"""

def camera():
    cap = cv2.VideoCapture(-1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    model = torch.hub.load("ultralytics/yolov5", "custom", path = "i2e2_best_v6.pt", force_reload=True)

    model.conf = 0.2

    def show_camera():
        window_title = "i2e2"
        
        if cap.isOpened():
            try:
                window_handle = cv2.namedWindow(window_title, cv2.WINDOW_AUTOSIZE)
                while True:
                    success, frame = cap.read()
                
                    if cv2.getWindowProperty(window_title, cv2.WND_PROP_AUTOSIZE) >= 0:
                        # Make detections 
                        results = model(frame)
                        # 비디오 프레임 크기, 전체 프레임수, FPS 등 출력
                        print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
                        print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
                        print('Frame count:', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

                        fps = cap.get(cv2.CAP_PROP_FPS)
                        print('FPS:', fps)

                        # 검출된 객체화면 출력
                        cv2.imshow('i2e2', np.squeeze(results.render()))
                    else:
                        break 
                    keyCode = cv2.waitKey(10) & 0xFF
                    # Stop the program on the ESC key or 'q'
                    if keyCode == 27 or keyCode == ord('q'):
                        break
            finally:
                cap.release()
                cv2.destroyAllWindows()
        else:
            print("Error: Unable to open camera")


if __name__ == "__main__":

   
    camera()
    

