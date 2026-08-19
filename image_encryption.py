from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    arr = np.array(img)
    key = key % 256
    # XOR operation on each pixel
    arr = arr ^ key
    encrypted_img = Image.fromarray(arr)
    encrypted_img.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(image_path, key, output_path):
    # XOR is reversible, same function
    encrypt_image(image_path, key, output_path)
    print(f"Decrypted image saved as {output_path}")

if __name__ == "__main__":
    key = int(input("Enter Secret Key 1-255: "))
    encrypt_image("input.jpg", key, "encrypted.png")
    decrypt_image("encrypted.png", key, "decrypted.png")