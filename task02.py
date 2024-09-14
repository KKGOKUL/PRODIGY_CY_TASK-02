from PIL import Image

def encrypt_image(input_path, output_path, key=None):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Swapping red and blue channels
            encrypted_pixel = (b, g, r)

            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key=None):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Swapping red and blue channels back
            decrypted_pixel = (b, g, r)

            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image decrypted successfully!")

if __name__ == "__main__":
    # Image paths
    input_image = r"C:\Users\Gokul\Pictures\ProdigyInfoTech_CyberSecurity-master\ProdigyInfoTech_CyberSecurity-master\Image Encryption\input.jpg"
    encrypted_image = r"C:\Users\Gokul\Pictures\ProdigyInfoTech_CyberSecurity-master\ProdigyInfoTech_CyberSecurity-master\Image Encryption\encrypted_img.jpg"
    decrypted_image = r"C:\Users\Gokul\Pictures\ProdigyInfoTech_CyberSecurity-master\ProdigyInfoTech_CyberSecurity-master\Image Encryption\decrypted_img.jpg"

    # Ask the user whether to encrypt or decrypt
    action = input("Do you want to (e)ncrypt or (d)ecrypt the image? ").strip().lower()

    if action == 'e':
        # Encrypt the image
        encrypt_image(input_image, encrypted_image, key=None)
    elif action == 'd':
        # Decrypt the image
        decrypt_image(encrypted_image, decrypted_image, key=None)
    else:
        print("Invalid option. Please choose 'e' to encrypt or 'd' to decrypt.")
