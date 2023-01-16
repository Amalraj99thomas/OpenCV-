#open an image in its own window using a python script 

import cv2

img = cv2.imread('00-puppy-Copy1.jpg')

#while and True are case sensitive
while True: 
    
    cv2.imshow('Dog', img)

    # If waited for atleast 1 ms AND the ESC key is entered
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()