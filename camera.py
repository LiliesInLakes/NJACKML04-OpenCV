import cv2 as cv
import numpy as np

camera= cv.VideoCapture(0)
frame_width = int(camera.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = camera.get(cv.CAP_PROP_FPS) 
out = cv.VideoWriter('/Users/avni/Downloads/mine1.mp4', cv.VideoWriter_fourcc(*'mp4v'), 16.0, (frame_width, frame_height))
while True:
        ret, frame = camera.read() # Read a frame

        if not ret:
            print("Error: Failed to read frame.")
            break
        fliped= cv.flip(frame, 1)
        
        out.write(fliped)
        #fourcc = cv2.VideoWriter_fourcc(*'XVID') # Example for .avi
        # Or for .mp4:
        #fourcc = cv.VideoWriter_fourcc(*'MJPEG')
        
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        blurred = cv.GaussianBlur(gray, (5, 5), 0)  # Step 1: Smooth out noise
        edges = cv.Canny(blurred, 100, 200)  # Step 2: Extract clean edges
        cv.imshow('Camera Feed', edges) # Display the frame
        # Press 'q' to exit the loop
        if cv.waitKey(50) & 0xFF == ord('q'):
            break
camera.release()
out.release()
cv.destroyAllWindows()
