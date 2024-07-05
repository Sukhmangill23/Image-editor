from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os

# Replace these with the correct folders for your unedited and edited images
path = "path/to/your/unedited/images"
pathOut = "path/to/your/edited/images"

# Ensure the output directory exists
os.makedirs(pathOut, exist_ok=True)

for filename in os.listdir(path):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
        img = Image.open(f"{path}/{filename}")

        # Apply a sharpening filter
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
