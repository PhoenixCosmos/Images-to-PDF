from PIL import Image
import os
import re

def natural_sort_key(filename):
    return [
        int(text) if text.isdigit() else text.lower()
        for text in re.split(r'(\d+)', filename)
    ]
def folder():
    while True:
        input_folder = input("Enter input folder path: ").strip()

        if os.path.isdir(input_folder):
            return input_folder

        print("Folder does not exist. Please enter a valid folder path.")


def filetopdf():
	while True:          
		# Get folder path
		input_folder = folder()

		# Supported image extensions
		extensions = (".png", ".jpg", ".jpeg", ".bmp", ".webp")
		

		# Get image files and sort alphabetically
		image_files = sorted(
			[f for f in os.listdir(input_folder) if f.lower().endswith(extensions)],
			key=natural_sort_key
		)

		if not image_files:
			print("No images found.")
			return

		images = []

		for file in image_files:
			path = os.path.join(input_folder, file)

			# Open image and convert to RGB (required for PDF)
			img = Image.open(path).convert("RGB")
			images.append(img)

		output_pdf = input_folder + ".pdf"

		# Save first image and append the rest
		images[0].save(
			output_pdf,
			save_all=True,
			append_images=images[1:]
		)

		print(f"Created {output_pdf} with {len(images)} pages.")


filetopdf()