from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np

# Set the dimensions of the images and video
image_width, image_height = 640, 480

# Create a list to store the frames
frames = []

# Iterate through each image
for i in range(40):
    # Create a blank image
    img = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(img)

    # Load the current image
    file_counter = f'{i+1:04d}'
    current_image = Image.open(f'../assets/photos/png/2023-08-v10_{file_counter}.png')  # Replace with your actual file path

    # Calculate the position for the current image layer
    position = (i * 3, i * 3)

    # Paste the current image onto the blank image
    img.paste(current_image, position)

    # Append the current frame to the list
    frames.append(np.array(img))  # Convert to NumPy array for displaying with matplotlib

# Display each frame
for frame in frames:
    plt.imshow(frame)
    plt.axis('off')
    plt.show()
