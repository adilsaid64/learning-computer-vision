'''py script to display images in a seperate window.'''

import cv2

img = cv2.imread('../Data/d7d4071d-f5f6-4eea-a2c2-a613e9315d17.webp')

while True:
    cv2.imshow('Img', img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()