from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

file = "image.bmp"
density = 'Ñ@#W$9876543210?!abc;:+=-,._ ' # length 29
dark = 1
def greyscaleToAscii(pixel):
    return density[dark * (round(pixel/255)-1)]

# Load the image and convert to a NumPy array
img = np.asarray(Image.open(f"C:\\Users\\Alex\\OneDrive\\Code\\ASCII to Image\\{file}"))

# Apply the grayscale conversion using the weighted sum
gray_img = np.dot(img[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)

# Display the grayscale image
# plt.imshow(gray_img, cmap='gray')
# plt.axis('off')  # Hide the axes
# plt.show()
asciiImage = []
for row in gray_img:
    a = []
    for column in row:
        a.append(greyscaleToAscii(column))
    asciiImage.append(" ".join(a))

with open("asciiImage.txt","a") as file:
    for row in asciiImage:
        file.write(row + "\n")

