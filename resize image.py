from PIL import Image

# Open the image file
image = Image.open("/Users/thephaothutre/Desktop/pythonProject/Implement face recognition/Images/170089.png")

# Resize the image to a specific width and height
resized_image = image.resize((216, 216))

# Save the resized image
resized_image.save("170099.png")
