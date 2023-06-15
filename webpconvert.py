# Program to compress png to in a directory
from PIL import Image
import os

def compress_png(input_dir, output_dir):
    """Compresses all png files in input_dir and saves them in output_dir"""
    for file in os.listdir(input_dir):
        if file.endswith((".png", ".jpg", ".jpeg","jfif", ".bmp", ".tiff", ".tif")):
            print("Compressing file: " + file)
            Image.open(input_dir + file).save(output_dir + file[:-4] + ".webp")
        else:
            print("Skipping file: " + file)

compress_png(r'C:\Users\rohan\Desktop\BCA5\Image_to_Webp_Converter\input\\', r'C:\Users\rohan\Desktop\BCA5\Image_to_Webp_Converter\output\\')

