from PIL import Image

# Open an image file
image_path = 'snake.png'
with Image.open(image_path) as img:
    # Output original size
    print(f'Original size: {img.size}')

    # Set the base width or height
    base_width = 400  # You can adjust this value as needed

    # Calculate the height using the aspect ratio
    w_percent = (base_width / float(img.size[0]))
    h_size = int((float(img.size[1]) * float(w_percent)))

    # Resize image
    img_resized = img.resize((base_width, h_size))

    # Output new size
    print(f'Resized image size: {img_resized.size}')

    # Save the resized image
    img_resized.save('resized_image.jpg')

