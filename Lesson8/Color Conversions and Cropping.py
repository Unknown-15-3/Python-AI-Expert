import cv2
import matplotlib.pyplot as plt

image = cv2.imread("Lesson8\\dark.jpg")

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB image")
plt.show()

gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_scale, cmap = "gray")
plt.title("Gray scale image")
plt.show()

cropped_image = image[100:200, 100:200]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped RGB image")
plt.show()