import math
import os
from PIL import Image

# User input - specify the folder containing the images

# inputs

folder_path = "C:/Users/rahul/Desktop/testing"
default = {
    'width': 800,
    'quality': 30,
    'crop_position_num': 22,
}

# Get a list of all the image files in the folder
img_list = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if
            f.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]
img_list = [f.replace("\\", "/") for f in img_list]  # Replace Windows-style path separator with Unix-style separator



# Iterate through the list of images

for imgURL in img_list:

    # ratio = '9X16'.split('X')

    # Naming image
    imgFolder = imgURL.split('/')
    imgName = imgFolder[-1].split('.')[0]
    imgExt = imgFolder[-1].split('.')[1]
    del imgFolder[-1]
    imgFolder = '/'.join(imgFolder)

    # Create the subdirectory for the compressed images
    comp_folder_path = imgFolder + "/compressed images"
    os.makedirs(comp_folder_path, exist_ok=True)

    # Load the original image
    image = Image.open(imgURL)

    # Get the width and height of the original image
    width, height = image.size

    # Set the desired size of the resized image
    # new_size = (900, 1600)
    try:
        new_width = int(input(f"Enter the width of {imgName} image: "))

    except:
        new_width = default['width']
        print(f'taking default value of width: {new_width}')

    # calculate new height based on new width
    new_height = math.floor((height / width) * new_width)

    if width < new_width:
        new_width = width
        new_height = height

    # resize the image
    resized_image = image.resize((new_width, new_height), resample=Image.LANCZOS)

    # Set the quality of the saved images function to a value between 1 and 95.
    try:
        quality = int(input("Set quality from 1 to 95:"))
        if 95 >= quality >= 1:
            quality = default['quality']
    except:

        quality = default['quality']
        print(f'taking default value of quality: {quality}')

    comp_path = comp_folder_path + f"/{imgName}.{imgExt}"
    resized_image.save(comp_path, optimize=True, quality=quality)
    print("\nCompleted the process and saved image successfully \n \n")


