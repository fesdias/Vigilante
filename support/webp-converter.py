from PIL import Image
import os

def compress_and_convert_to_webp(input_path, output_path, quality=85):
    """
    Compresses an image and converts it to WebP format.

    Parameters:
    - input_path: The path to the input image file.
    - output_path: The path to save the output WebP file.
    - quality: The quality of the WebP image (0-100, default is 85).
    """
    try:
        # Open the image
        img = Image.open(input_path)

        # Save the compressed image in WebP format
        img.save(output_path, "WEBP", quality=quality)

        print(f"Image compressed and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def batch_compress_and_convert_to_webp(input_folder, output_folder, quality=85):
    """
    Batch compresses and converts all images in a folder to WebP format.

    Parameters:
    - input_folder: The path to the folder containing input images.
    - output_folder: The path to save the output WebP files.
    - quality: The quality of the WebP images (0-100, default is 85).
    """
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each file in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Check if the file is an image
        if os.path.isfile(input_path) and any(input_path.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg']):
            # Generate output path by changing the extension to .webp
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.webp')

            # Compress and convert the image
            compress_and_convert_to_webp(input_path, output_path, quality)

# Example usage:
input_folder = "/Users/felipedias/Downloads/Vigilante/Site/Code/assets/gallery/vigilante_01_004/png"
output_folder = "/Users/felipedias/Downloads/Vigilante/Site/Code/assets/gallery/vigilante_01_004/webp"
batch_compress_and_convert_to_webp(input_folder, output_folder, quality=85)
