import cv2
import numpy as np
import os

def histogram_color_equalize(image):
    channels = cv2.split(image)

    equalized_channels = [cv2.equalizeHist(channel) for channel in channels]

    equalized_image = cv2.merge(equalized_channels)

    return equalized_image

def main():
    image_path = input("Enter the path for image: ")

    before_image = cv2.imread(image_path)

    if before_image is None:
        print("Error: Invalid input")
        return

    # Apply histogram equalization to each color channel
    after_image = histogram_color_equalize(before_image)

    image_dir, image_name = os.path.split(image_path)

    result_path = os.path.join(image_dir, "after-" + image_name)

    cv2.imwrite(result_path, after_image)

    # Display the before and after images
    cv2.imshow("Before Image", before_image)
    cv2.imshow("After Image", after_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
