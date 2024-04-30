import cv2
import numpy as np

def upscale_image(image_path, scale_factor=2):
    
    image = cv2.imread(image_path)
    
    
    upscaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)
    
    return upscaled_image

def sharpen_image(image):
    
    kernel = np.array([[-1, -1, -1],
                       [-1, 10, -1],
                       [-1, -1, -1]])
    
    
    sharpened_image = cv2.filter2D(image, -1, kernel)
    
    return sharpened_image

def smooth_edges(image, d, sigma_color, sigma_space):
    
    smoothed_image = cv2.bilateralFilter(image, d, sigma_color, sigma_space)
    
    return smoothed_image

d = 9  
sigma_color = 75  
sigma_space = 75

input_image_path = input('Enter Cropped image path (eg., ./detections/crop/cars/frame_150/licence_plate_1.png) :-')  
output_image_path = 'upscaled_image.jpg'  
upscaled_image = sharpen_image(upscale_image(input_image_path, scale_factor=4))


cv2.imwrite(output_image_path, upscaled_image)


cv2.imshow('Original Image', cv2.imread(input_image_path))
cv2.imshow('Upscaled Image', upscaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
