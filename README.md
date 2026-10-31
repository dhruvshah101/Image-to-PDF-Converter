# Image to PDF Converter

A simple Python program that allows users to select multiple images from a directory and combine them into a single PDF file.

## Features
- Automatically detects JPG, JPEG, and PNG images in a specified directory.
- Displays a numbered list of available images.
- Allows users to select multiple images by entering their corresponding numbers.
- Combines selected images into a single PDF.
- Automatically converts images to RGB format for PDF compatibility.

## Requirements
- Python 3
- Pillow (PIL)

Install Pillow using:

```bash
pip install Pillow
```

## How to Use

1. Run the Python script.
2. Enter the directory containing your images (e.g., `~/Downloads`).
3. View the numbered list of available images.
4. Enter the numbers of the images you want to combine, separated by commas (e.g., `1, 3, 5`).
5. The program generates a PDF named `combined.pdf` in the current working directory.

## Example

```text
Enter directory (e.g. ~/Downloads): ~/Downloads

Available Images:
1. image1.png
2. image2.jpg
3. image3.jpeg

Enter image numbers (separated by commas): 1, 2, 3

PDF Successfully Created!
```

## Technologies Used
- **Python** – Core programming language
- **Pillow (PIL)** – Image processing and PDF generation
- **OS** – Directory navigation and file management

## Output

The program creates a `combined.pdf` file containing the selected images in the order they were entered.
