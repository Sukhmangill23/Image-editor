from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os

path = "/Users/sukhmandeep/Documents/Photos"  # Replace with the correct folder for unedited images
pathOut = "/Users/sukhmandeep/Documents/editedimgs"  # Replace with the correct folder for edited images

# Ensure the output directory exists
# Ensure the output directory exists
os.makedirs(pathOut, exist_ok=True)

for filename in os.listdir(path):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
        img = Image.open(f"{path}/{filename}")

        # Sharpening, converting to black and white, and rotating
        edit = img.filter(ImageFilter.SHARPEN)

        # Optionally convert to black and white (comment out if color is desired)
        # edit = edit.convert('L')

        # Rotate the image
        edit = edit.rotate(-90)

        # Enhance contrast
        factor = 1.1
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(factor)

        # Resize the image
        edit = edit.resize((1800, 1200))

        # Add a border
        border = 1
        edit = ImageOps.expand(edit, border=border, fill='black')

        # Save the edited image
        clean_name = os.path.splitext(filename)[0]
        edit.save(f'{pathOut}/{clean_name}_edited.jpg')

print("Editing complete.")
