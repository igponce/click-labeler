# import the necessary packages
import argparse
import cv2
import numpy as np
from scipy.ndimage import zoom
from skimage.transform import resize

# initialize the list of reference points and state
points = []
state = 'click_loop'
filename='foto'

def click_loop (event, x, y, flags, param):
    # grab references to the global variables
    global points

    # Point = Left button UP
    if event == cv2.EVENT_LBUTTONUP:
        points.append((x, y))
        
        # draw a point
        cv2.circle(image, (x,y) , 5, (0,255,0), 3) 
        cv2.putText(image,str(len(points)),(x+1,y+1), 1, 2,(0,0,0),2,cv2.LINE_AA)
        cv2.putText(image,str(len(points)),(x,y), 1, 2,(255,255,255),2,cv2.LINE_AA)
        cv2.imshow(filename, image)
        print("Point @: {} {}".format(x,y)) 

 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image, clone it, and setup the mouse callback function

filename = args["image"]
image = cv2.imread(filename) 
# image = zoom( image, 300/image.shape[0], np.uint8 )
image = resize( image, (400,400) )
clone = image.copy()

cv2.namedWindow(filename)
cv2.setMouseCallback(filename, click_loop)

print("""Instructions:

  r   - RESET
  q   - QUIT without saving
  s,x - (s)AVE, E(x)IT saving results to filename.points

  File: {}
""".format(filename) )

# Loop until keyboard exit
while True:
    # display the image and wait for a keypress
    cv2.imshow(filename, image)
    key = cv2.waitKey(1) & 0xFF

    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        image = clone.copy()
        points = []
        print("Reset")

    if key == ord('q'):
        print("QUIT without saving");
        state = "QUIT"
        break;

    if key == ord('x') or key==ord('s'):
        if len(points) > 0 :
           state = "SAVE"
        else :
           state = "QUIT"
           print("Not enough points. QUITTING")
        break;


if state == "SAVE" :
    pointStr = "|".join([ "{},{}".format(p[0]/image.shape[1],p[1]/image.shape[0]) for p in points ] )
    outfile = "{}.points".format(filename)
    print("SAVING points")
    with open(outfile, "w") as fp:
       fp.write(pointStr)
       fp.close()

# close all open windows
cv2.destroyAllWindows()
