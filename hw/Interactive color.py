import argparse
from pathlib import Path

import cv2


WINDOW_NAME = "Interactive Color Filter"
TRACKBAR_WINDOW = "HSV Controls"


def load_image(image_path: str):
	path = Path(image_path).expanduser()
	image = cv2.imread(str(path))
	if image is None:
		raise FileNotFoundError(f"Could not read image: {path}")
	return image


def create_trackbars() -> None:
	cv2.namedWindow(TRACKBAR_WINDOW)
	controls = (
		("H min", 0, 179),
		("H max", 179, 179),
		("S min", 0, 255),
		("S max", 255, 255),
		("V min", 0, 255),
		("V max", 255, 255),
	)
	for name, value, maximum in controls:
		cv2.createTrackbar(name, TRACKBAR_WINDOW, value, maximum, lambda _: None)


def get_hsv_limits():
	"""Return the current lower and upper HSV limits."""
	lower = [
		cv2.getTrackbarPos("H min", TRACKBAR_WINDOW),
		cv2.getTrackbarPos("S min", TRACKBAR_WINDOW),
		cv2.getTrackbarPos("V min", TRACKBAR_WINDOW),
	]
	upper = [
		cv2.getTrackbarPos("H max", TRACKBAR_WINDOW),
		cv2.getTrackbarPos("S max", TRACKBAR_WINDOW),
		cv2.getTrackbarPos("V max", TRACKBAR_WINDOW),
	]
	return lower, upper


def apply_color_filter(image, lower, upper):
	"""Create a mask and filtered image for the selected HSV range."""
	hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv_image, lower, upper)
	filtered = cv2.bitwise_and(image, image, mask=mask)
	return mask, filtered


def show_results(original, mask, filtered) -> None:
	"""Display the original image, mask, and filtered result."""
	cv2.imshow("Original", original)
	cv2.imshow("Mask", mask)
	cv2.imshow(WINDOW_NAME, filtered)


def run_filter(image) -> None:
	"""Run the interactive filter loop for one static image."""
	create_trackbars()
	while True:
		lower, upper = get_hsv_limits()
		mask, filtered = apply_color_filter(image, lower, upper)
		show_results(image, mask, filtered)

		key = cv2.waitKey(30) & 0xFF
		if key in (ord("q"), 27):
			break
	cv2.destroyAllWindows()


def parse_arguments():
	parser = argparse.ArgumentParser(description="Interactively filter colours in an image.")
	parser.add_argument("image", help="Path to the static image")
	return parser.parse_args()


def main() -> None:
	args = parse_arguments()
	image = load_image(args.image)
	run_filter(image)


if __name__ == "__main__":
	main()

