import cv2
import numpy as np
# Usage
def solution(image_path):
    image= cv2.imread(image_path)


    ######################################################################
    ######################################################################
    #####  WRITE YOUR CODE BELOW THIS LINE ###############################

    
    

    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    
    largest_area=0
    largest_quadrilateral=None

    
    for contour in contours:
        epsilon=0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        if len(approx) == 4:
            area=cv2.contourArea(approx)
            
            if area>largest_area:
                largest_area=area
                largest_quadrilateral=approx
            
            
    if largest_quadrilateral is not None:
        largest_quadrilateral_coordinates = np.array(largest_quadrilateral)
    
    pts2 = np.float32([[0, 0], [600, 0], [600, 600],[0, 600]])
    quadrilateral_points=largest_quadrilateral_coordinates.reshape(-1,2)

   # print(quadrilateral_points)
    
    
    #quadrilateral_points=sort_vertices_anticlockwise(quadrilateral_points)
    #to sort the vertices in ACW direction 
    centroid = np.mean(quadrilateral_points, axis=0)
    angles = np.arctan2(quadrilateral_points[:, 1] - centroid[1], quadrilateral_points[:, 0] - centroid[0])
    sorted_indices = np.argsort(angles)
    sorted_vertices = quadrilateral_points[sorted_indices]
    sorted_vertices=np.float32(sorted_vertices)
        
    


    matrix=cv2.getPerspectiveTransform(sorted_vertices,pts2)
    result=cv2.warpPerspective(image,matrix,(600,600))
    
    sharpening_kernel = np.array([[-1, -1, -1],
                               [-1,  9, -1],
                               [-1, -1, -1]])
    
    sharpened_image = cv2.filter2D(result, -1, sharpening_kernel)
    white_threshold = 200  # Adjust this threshold as needed
    mask = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY) < white_threshold
    result_image = result.copy()
    result_image[mask] = sharpened_image[mask]


    result_image = cv2.addWeighted(result, 0.999, result_image, 0.001, 0)
    # cv2.imshow('Sharpened Image', result_image)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    

    

    ######################################################################
    return result_image




 
# rss=solution('/Users/netrajrane/Downloads/Assignment 1 2/Q1/test/15.png')

# sharpening_kernel = np.array([[-1, -1, -1],
#                                [-1,  9, -1],
#                                [-1, -1, -1]])
    
# sharpened_image = cv2.filter2D(rss, -1, sharpening_kernel)
# cv2.imshow('Original Image', rss)
# # cv2.imshow('Sharpened Image', sharpened_image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ################### largest contour and 4 sides contour 
