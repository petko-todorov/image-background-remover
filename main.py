import os

input_dir = input("Input directory (leave empty to use current directory): ").strip()
input_dir = input_dir if input_dir else os.getcwd()

print(f"Processing images in: {input_dir}")

all_files = os.listdir(input_dir)

image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
image_files = [f for f in all_files if f.lower().endswith(image_extensions)]
if not image_files:
    exit("No image files found in this directory.")

output_dir = os.path.join(input_dir, 'Output')

