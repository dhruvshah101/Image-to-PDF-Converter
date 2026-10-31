from PIL import Image
import os

# Ask user for a directory
directory = input("Enter directory (e.g. ~/Downloads): ").strip()
directory = os.path.abspath(os.path.expanduser(directory))

if os.path.isdir(directory):

    # Retrieve only PNG and JPG files
    images = [
        filename for filename in os.listdir(directory)
        if filename.lower().endswith((".png", ".jpg" , ".jpeg"))
        and os.path.isfile(os.path.join(directory, filename))
    ]

    # Display numbered list of images
    print("\nAvailable Images:")
    for i, filename in enumerate(images, start=1):
        print(f"{i}. {filename}")

    # Ask user to select images
    selections = input("\nEnter image numbers (separated by commas): ")

    # Store selected files in an array
    selected_files = []

    for number in selections.split(","):
        index = int(number.strip()) - 1

        if 0 <= index < len(images):
            selected_files.append(os.path.join(directory, images[index]))
        else:
            print(f"Invalid selection: {number}")

else:
    print("Directory not found.")

images = []

for file in selected_files:
    img = Image.open(file).convert("RGB")
    images.append(img)

if images:
    images[0].save("combined.pdf", save_all = True, append_images =images[1:])
    print("PDF Succesfully Created!")
else:
    print("Image(s) not found.")
