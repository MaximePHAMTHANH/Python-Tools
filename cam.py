import cv2

# Open the default camera
print("Press Q to exit")
cam = cv2.VideoCapture(1)
if not cam.isOpened() : 
	cam = cv2.VideoCapture(0)
	print('No USB WebCam detected, opening default Cam')

# Get the default frame width and height
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH)*1.6)
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)*1.6)

# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

while True:
    ret, frame = cam.read()

    # Write the frame to the output file
    # out.write(frame)

    # Display the captured frame
    resize = cv2.resize(frame, (frame_width, frame_height))
    cv2.imshow('Camera', resize)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and writer objects
cam.release()
# out.release()
cv2.destroyAllWindows()