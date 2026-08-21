import cv2
import numpy as np

def apply_colour_filter(image, filter_type):
    filtered_image = image.copy()

    if filter_type == 'red_tint':
        filtered_image[:,:,1] = 0
        filtered_image[:,:,0] = 0
    elif filter_type == 'blue_tint':
        filtered_image[:,:,1] = 0
        filtered_image[:,:,2] = 0
    elif filter_type == 'green_tint':
        filtered_image[:,:,0] = 0
        filtered_image[:,:,2] = 0
    elif filter_type == "increase_Red":
        filtered_image[:,:,2] = cv2.add(filtered_image[:,:,2], 50)
    elif filter_type == "decrease_Blue":
        filtered_image[:,:,0] = cv2.subtract(filtered_image[:,:,0], 50)

    return filtered_image

image_path = ("lesson11\\nature.jpg")
image = cv2.imread(image_path)
if image is None:
    print("Error! image not found")
else:
    filter_type = "original"
    print("press the following filteres keys to apply:")
    print("r-red tint")
    print("b-blue tint")
    print("g-green tint")
    print("i- increase red intensity")
    print("d- decrease blue intensity")
    print("q- quit")

    while True:
        filtered_image = apply_colour_filter(image, filter_type)
        cv2.imshow("filtered image", filtered_image)
        key = cv2.waitKey(0) & 0xFF

        if key == ord("r"):
            filter_type = "red_tint"
        elif key == ord("b"):
            filter_type = "blue_tint"
        elif key == ord("g"):
            filter_type = "green_tint"
        elif key == ord("i"):
            filter_type = "increase_red"
        elif key == ord("d"):
            filter_type = "decrease_blue"
        elif key == ord("q"):
            print("E..X..I..T..I..N..G")
            break
        else:
            print("Invalid key! please try again and use 'r', 'b', 'g', 'i', 'd', 'q' ")

cv2.destroyAllWindows()