import os
from rembg import remove, new_session
from PIL import Image

MODEL_1 = "isnet-general-use"
MODEL_2 = "u2netp"

input_dir = input("Input directory (leave empty to use current directory): ").strip()
input_dir = input_dir if input_dir else os.getcwd()

print(f"Processing images in: {input_dir}\n")

image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')
all_files = os.listdir(input_dir)
image_files = [f for f in all_files if f.lower().endswith(image_extensions)]

if not image_files:
    exit("No image files found in this directory.")

output_dir = os.path.join(input_dir, 'Output')
os.makedirs(output_dir, exist_ok=True)

session1 = new_session(model_name=MODEL_1)
session2 = new_session(model_name=MODEL_2)


def count_non_transparent_pixels(image):
    """Count how many pixels are not fully transparent in an RGBA image."""
    alpha = image.getchannel('A')
    return sum(1 for pixel in alpha.getdata() if pixel > 10)  # slight threshold helps ignore soft transparency


for image_file in image_files:
    input_path = os.path.join(input_dir, image_file)
    output_name = os.path.splitext(image_file)[0] + '.png'
    output_path = os.path.join(output_dir, output_name)

    print(f"Processing: {image_file}")

    try:
        img = Image.open(input_path).convert("RGBA")

        output1 = remove(img, session=session1)
        output2 = remove(img, session=session2)

        count1 = count_non_transparent_pixels(output1)
        count2 = count_non_transparent_pixels(output2)

        if count1 >= count2:
            chosen = output1
            model_used = MODEL_1
            print(f'Used model {MODEL_1}')
        else:
            chosen = output2
            model_used = MODEL_2
            print(f'Used model {MODEL_2}')

        chosen.save(output_path, format="PNG")
        print(f"Saved to: {output_path}\n")

    except Exception as e:
        print(f"Could not process {image_file}: {e}\n")
