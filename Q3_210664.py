import cv2
import numpy as np

def solution(image_path):
    ############################
    ############################

    ############################
    ############################
    ## comment the line below before submitting else your code wont be executed##
    # pass
    image = cv2.imread(image_path)
    height, width = image.shape[:2]
    # new_width = width * 2
    # new_height = height * 2
    image=cv2.resize(image, (width*2, height*2))

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply edge detection to the grayscale image (e.g., using the Canny edge detector)
    edges = cv2.Canny(gray, 50 , 150, apertureSize=3)
    flick=0
    
    lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=150)
    if lines is not None:
     longest_line = None
     max_length = 0

     for rho, theta in lines[:, 0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        
        # Calculate the length of the line
        length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        if length > max_length:
            max_length = length
            longest_line = (x1, y1, x2, y2)

        


     if longest_line is not None:
        x1, y1, x2, y2 = longest_line


        # Calculate the angle of the longest line with the vertical axis
        angle_rad = np.arctan2(y1 - y2, x1 - x2)
        angle_deg = np.degrees(angle_rad)
        if(angle_deg<0):
            angle_deg=-angle_deg
            flick=1



        # print("Longest line length:", max_length)
        # print("Angle with vertical (degrees):", angle_deg)
        # height, width = image.shape[:2]
        # center = (width // 2, height // 2)
        
        
        
        
       
        
        
        
        if(angle_deg<90):
            angle_deg=90-angle_deg
        
        if(angle_deg>=90):
            angle_deg=180-angle_deg
            
            
        if(flick==0):
            angle_deg=-angle_deg
        
        
        ########################
        
        height, width=image.shape[:2]

        canvas_height, canvas_width = height * 2, width * 2
        canvas = np.full((canvas_height, canvas_width, 3), 255, dtype=np.uint8)


        # Calculate the position to place the image in the center of the canvas
        x_offset = (canvas_width - width) // 2
        y_offset = (canvas_height - height) // 2

        # Place the image on the canvas
        canvas[y_offset:y_offset + height, x_offset:x_offset + width] = image

        # Define the center of rotation
        center = (canvas_width // 2, canvas_height // 2)
        border_value = (255, 255, 255) 

        # Rotate the canvas by the specified angle
        rotation_matrix = cv2.getRotationMatrix2D(center, angle_deg, 1.0)
        rotated_image = cv2.warpAffine(canvas, rotation_matrix, (canvas_width, canvas_height), borderMode=cv2.BORDER_CONSTANT, borderValue=border_value)

    
        #######################################
        
        # height, width=image.shape[:2]
        # center=(width//2,height//2)
        # border_value = (255, 255, 255)  # White color
        # rotation_matrix = cv2.getRotationMatrix2D(center, angle_deg, 1.0)
        # rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height),borderMode=cv2.BORDER_CONSTANT, borderValue=border_value)
        
        # rotated_height, rotated_width = rotated_image.shape[:2]
        # canvas_height, canvas_width = int(1.5 * rotated_height), int(1.5 * rotated_width)

        # # Create a blank canvas of the calculated size
        # canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

        # x_offset = (canvas_width - rotated_width) // 2
        # y_offset = (canvas_height - rotated_height) // 2

        # canvas[y_offset:y_offset + height, x_offset:x_offset + width] = image
        # cv2.imshow('solution', canvas)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

            
        
        
        
        
        sharpening_kernel = np.array([[-1, -1, -1],[-1,  9, -1], [-1, -1, -1]])
        sharpened_image = cv2.filter2D(rotated_image, -1, sharpening_kernel)  
        gray2 = cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('imag',gray2)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        thresh2 = cv2.threshold(gray2, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (45,1))
        morph = cv2.morphologyEx(thresh2, cv2.MORPH_DILATE, kernel)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (60,50))
        morph = cv2.morphologyEx(thresh2, cv2.MORPH_DILATE, kernel)
        # cv2.imshow('imorge',image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        
        contours,_ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)        
        
        
        if len(contours) > 0:
            # Find the largest contour (assuming you have multiple)
            largest_contour = max(contours, key=cv2.contourArea)
            M = cv2.moments(largest_contour)
    
            if M["m00"] != 0:
                centroid_x = int(M["m10"] / M["m00"])
                centroid_y = int(M["m01"] / M["m00"])
            else:
                centroid_x, centroid_y = 0, 0

            max_y = np.max(largest_contour[:, :, 1])
            min_y = np.min(largest_contour[:, :, 1])
            
            
        avg=max_y+min_y
        avg=avg/2
        # print(avg)
        # print(centroid_y)
        if(avg<centroid_y):
            rotated_image = cv2.rotate(rotated_image, cv2.ROTATE_180)

            
            

        
        
        
        
        
        
    
        # cv2.imshow('solution',rotated_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        
        
        
        return rotated_image


# cv2.imshow('solution',solution('/Users/netrajrane/Downloads/Assignment 1 2/Q3/test/3_c.png'))
# cv2.waitKey(0)
# cv2.destroyAllWindows()