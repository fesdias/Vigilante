from PIL import Image, ImageDraw
import imageio
import os

def create_frame(depth, layers, initial_frame, folder, collection):
    # Set the dimensions of the final image
    image_width, image_height = (768 + (layers * depth)), (512 + (layers * depth))

    # Create a blank image
    final_image = Image.new('RGBA', (image_width, image_height), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(final_image)

    # Define the starting position for the first image
    start_x, start_y = 0, 0

    # Create individual frame
    for i in range(layers):

        # Calculate loop
        if i < initial_frame:
            img_index = layers - (initial_frame - i)
        else:
            img_index = i - initial_frame

        # Load the current image
        file_counter  = f'{img_index:04d}'
        file_name     = f'{collection}_{file_counter}.png'
        current_image = Image.open(f'{folder}/png/{file_name}')

        # Calculate the position for the current image layer
        position = (start_x + i * depth, start_y + i * depth)

        # Paste the current image onto the final image
        final_image.paste(current_image, position)

    # Save or display the final image
    file_name = f'{folder}/animation/frames/frame_{initial_frame:04d}.png'
    final_image.save(file_name)
    return file_name


def create_video(frames, output_video):
    # Save the frames as a video
    imageio.mimsave(output_video, frames, format='webm', codec='vp9', fps = 10)


depth = 4
layers = 40
frames = []

collection = "vigilante_01_004"
folder = f"../assets/gallery/{collection}"

# Create output folder if it doesn't exist
if not os.path.exists(f"{folder}/animation"):
    os.makedirs(f"{folder}/animation")

if not os.path.exists(f"{folder}/animation/frames"):
    os.makedirs(f"{folder}/animation/frames")

# CREATE INDIVIDUAL FRAMES
for initial_frame in range(40):
    new_frame = create_frame(depth, layers, initial_frame, folder, collection)
    frames.append(imageio.imread(new_frame))
    print(f'Done! {new_frame}')

# # If images are already created
# for i in range(40):
#     file_name = f'{folder}/animation/frames/frame_{i:04d}.png'
#     frames.append(imageio.imread(file_name))

output_file = f'{folder}/animation/{collection}.webm'
create_video(frames, output_file)
print("Animation Done! xD")