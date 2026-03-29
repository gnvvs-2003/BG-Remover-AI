from rembg import remove
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Hide the main tkinter window
root = tk.Tk()
root.withdraw()

# Ask user to select input file
input_path = filedialog.askopenfilename(
	title="Select input image",
	filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff;*.webp")]
)
if not input_path:
	messagebox.showerror("Error", "No input file selected.")
	exit(1)


# Ask user to select output file name and location
output_path = filedialog.asksaveasfilename(
	title="Save output image as",
	defaultextension=".png",
	filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg;*.jpeg"), ("All Files", "*.*")]
)
if not output_path:
	messagebox.showerror("Error", "No output file selected.")
	exit(1)

try:
	input_image = Image.open(input_path)
	output_image = remove(input_image)
	output_image.save(output_path)
	messagebox.showinfo("Success", f"Background removed!\nSaved to: {output_path}")
	os.startfile(output_path)
except Exception as e:
	messagebox.showerror("Error", f"Failed to process image:\n{e}")