from PIL import Image
import numpy as np

def encrypt_decrypt_image(image_path, key, output_path):
    # 1. Image ko load karo
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # 2. XOR operation har pixel pe karo
    encrypted_array = img_array ^ key
    
    # 3. Wapas image me convert karke save karo
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)
    print(f"Saved: {output_path}")

def main():
    input_file = "input.jpg"  # tumhari wali photo
    
    key = int(input("Enter Secret Key 1-255: "))
    key = key % 256  # 0-255 ke beech me rahe

    # Encrypt karo
    encrypt_decrypt_image(input_file, key, "encrypted.png")
    
    # Decrypt karo - wapas XOR karne se original aa jayega
    encrypt_decrypt_image("encrypted.png", key, "decrypted.png")
    
    print("Done! Check encrypted.png and decrypted.png")

if __name__ == "__main__":
    main()