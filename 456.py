import cv2
import numpy as np

# 이미지를 불러옵니다.
img = cv2.imread('C:\\Users\pyeonmu\Desktop/picture1.png')

# Initialize control parameters
kernel_size = 9
sigma_color = 150
sigma_space = 2.4
n_iterations = 1
img_select = 0
img_list = ['C:\\Users\pyeonmu\Desktop/picture1.png']
# Apply the bilateral filter iteratively
#result = img.copy()

while True:
    # Read the given image
    img = cv2.imread(img_list[img_select])
    # Apply the median filter
    result = cv2.medianBlur(img, kernel_size)

    # 결과를 출력합니다.
    
    
    # Show all images
    merge = np.hstack((img, result))
    cv2.imshow('Medial Filter: Original | Result', merge)

    # Process the key event
    key = cv2.waitKey()
    if key == 27: # ESC
        break
    elif key == ord('+') or key == ord('='):
        kernel_size= kernel_size+2
    elif key == ord('-') or key == ord('_'):
        kernel_size= max(kernel_size-2,3)
    elif key == ord('\t'):
        img_select=(img_select+1)% len(img_list)

    # Show all images========================

cv2.destroyAllWindows()