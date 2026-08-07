import cv2
image = cv2.imread("lesson7\\nature pic.jpg")

cv2.namedWindow("Nature Pic", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Nature Pic", 800, 500)

cv2.imshow("Loaded Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Image dimesions: {image.shape}")
