import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
    plt.figure(figsize =(8,8))
    if len(image.shape) == 2:
        plt.imshow(image, cmap = 'gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def interactive_edge_detection(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: could not read the image.")
        return

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image("Original Image in gray scale", gray_image)
    print("Select an option")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Edge Detection")
    print("5. Median Edge Detection")
    print("6. Exit")
    while True:
        choice = input("enter your choice(1-6):")
        if choice == '1':
            sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize = 3)
            sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize = 3)
            sobel_combined = cv2.bitwise_or(sobel_x.astype(np.uint8), sobel_y.astype(np.uint8))
            display_image("sobel edge detection", sobel_combined)
        elif choice == '2':
            print("Adjust threshold for canny edge(default: 100, 200)")
            lower_threshold = int(input("enter lower threshold:"))
            upper_threshold = int(input("enter upper threshold:"))
            edges = cv2.Canny(gray_image, lower_threshold, upper_threshold)
            display_image("Canny Edge Detection", edges)
        elif  choice == '3':
            laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
            display_image("Laplacian edge detection", np.abs(laplacian).astype(np.uint8))
        elif choice == '4':
            print("Adjust kernal size for gaussian filter(must be odd, default:5)")
            kernal_size = int(input("enter kernal size:"))
            blurred = cv2.GaussianBlur(image, (kernal_size, kernal_size), 0)
            display_image("Gaussian Edge Detection", blurred)

        elif choice == '5':
            print("Adjust kernal size for median filter(must be odd, default:5)")
            kernal_size = int(input("enter kernal size:"))
            median = cv2.medianBlur(image, kernal_size)
            display_image("Median Edge Detection", median)
        elif choice == '6':
            print("Exitting....")
            break
        else:
            print("Invalid choice... retry")
interactive_edge_detection("lesson10\\Nature.jpg")