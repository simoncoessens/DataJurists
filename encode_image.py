import base64

# Function to encode file (image, font) to base64 and write to a text file
def encode_file_to_base64(file_path, output_file):
    with open(file_path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
        
    # Write the encoded string to a text file
    with open(output_file, "w") as text_file:
        text_file.write(encoded)
    print(f"Encoded file saved to {output_file}")

# Function to read the base64 string from a text file
def read_base64_from_file(file_path):
    with open(file_path, "r") as file:
        encoded_string = file.read()
    return encoded_string

# Specify the path of the font file and the output file for encoding
font_path = "TAN-MONCHERI.ttf"  # Replace with your .ttf file path
font_output_file = "encoded_moncheri.txt"

# Call the function to encode the font and save it to a text file
encode_file_to_base64(font_path, font_output_file)

# Specify the path of another file (e.g., image) and the output file
image_path = "landing.png"
image_output_file = "encoded_landing.txt"

# Call the function to encode the image and save it
encode_file_to_base64(image_path, image_output_file)

# Later, when you want to load and use the encoded font from the text file
font_base64 = read_base64_from_file(font_output_file)