import cv2 as cv
import numpy as np

# Input Image and Change It into Grayscale
inputImage = input("Enter the input image file name (add .jpg/.jpeg/.png): ")
image = cv.imread("inputImage\\" + inputImage, cv.IMREAD_GRAYSCALE)
image = np.array(image, dtype=np.int16)
w, h = image.shape[:2]

# Generate the Watermark
inputK = int(input("Enter the value of intensity (k): "))
inputSeed = int(input("Enter the seed: "))
num = np.random.seed(inputSeed)
watermark = np.random.randint(2, size = (w,h))
watermark = watermark.astype(np.int16)
watermark[watermark == 0] = -1
watermark = watermark * inputK

# Add the Watermark to the Image
watermarkedImage = cv.add(image, watermark)

# Save the Watermarked Image
outputImage = input("Enter the output image file name: ")
cv.imwrite(f'outputImage/{outputImage}.png', watermarkedImage)
print("Successfully saved the watermarked image!")

# Check if the Image is Watermarked
check = input("Do you want to check if the image is watermarked? (y/n): ")
while check != "y" and check != "n":
    print("Your input is invalid, please try again!")
    check = input("Do you want to check if the image is watermarked? (y/n): ")
if check == "y":
    print("Checking...")
    threshold = 100000
    diff = cv.absdiff(image, watermarkedImage)
    if np.sum(diff) > threshold:
        print("The result image is watermarked!")
    else:
        print("The result image is not watermarked!")
else:
    print("Program finished!")