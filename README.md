# Compress-N-Resize-bulk-images
#Powerfull tool for bluck images
This Python script takes a folder of images, resizes them to a desired width while maintaining the aspect ratio, reduces their quality, and saves them in a subdirectory called "compressed images"


Features:

1. With few noob modifications it can compress and resize unlimted images of different extensions on ONE CLICK
2. It creates a sub-directory (folder) within the images folder you provided
3. It will resize only when necessary otherwise it skips it

4.you can leave the input prompt blank to apply default or modify it to not ask prompt for each image  




This is what openai's chatGPT says about my script:


This is a Python script that compresses images in a specified folder by resizing them and reducing their quality. The following steps are performed by the script:

The user is prompted to enter the folder path containing the images to be compressed.

The script creates a list of all the image files in the specified folder with the file extensions .jpg, .jpeg, .png, .bmp, and .gif.

The script iterates through the list of image files and performs the following steps for each image:

a. The script gets the name, extension, and path of the image.

b. The script creates a subdirectory named "compressed images" in the same folder as the original image to store the compressed images.

c. The script loads the original image using the PIL library.

d. The script prompts the user to enter the desired width of the image. If the user enters an invalid input or leaves it blank, the default width of 800 pixels is used.

e. The script calculates the new height of the image based on the aspect ratio of the original image and the new width.

f. If the new width is greater than the original width, the script resizes the image to the original size.

g. The script resizes the image to the new width and height using the LANCZOS resampling method.

h. The script prompts the user to enter the desired quality of the compressed image as a value between 1 and 95. If the user enters an invalid input or leaves it blank, the default quality of 30 is used.

i. The script saves the compressed image in the "compressed images" subdirectory with the same name and extension as the original image.

j. The script prints a success message for each compressed image.

In summary, this script takes a folder of images, resizes them to a desired width while maintaining the aspect ratio, reduces their quality, and saves them in a subdirectory called "compressed images".
