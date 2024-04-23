import cv2
import numpy as np
import encryption


class ImageObj():

    def __init__(self,filepath):
        self.image = filepath
        self.isEncrypted = False
        self.encrypted_tag = None
        self.bytes = None
        self.aes_rsa_key = None
        

    def image_encryption(self):
        byte_array = self.image_to_bytes(self.image)
        data, nonce = self.aes_encryption(bytes(byte_array))
        self.bytes = data
        return nonce


    def image_decryption(self,nonce):
        if self.isEncrypted:
            image_bytes = self.aes_decryption(nonce)
            image_byte_array = bytearray(image_bytes)
            np_array = np.asarray(image_byte_array, dtype=np.uint8)
            decoded_image = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)
            cv2.imwrite('image_output1.jpg', decoded_image)
            self.encrypted = False
        else:
            print("image not encrypted")
    
    def image_to_bytes(self,image_encrypted):
        file = image_encrypted
        byteArray = np.fromfile(file, dtype=np.uint8)
        return byteArray

    
    def aes_encryption(self,message):
        cipher, tag, nonce ,key= encryption.aes_encrypt(message)
        aes_rsa_key = encryption.encrypt(key)
        e_tag = encryption.encrypt(tag)

        self.encrypted_tag = e_tag
        self.isEncrypted = True
        self.aes_rsa_key = aes_rsa_key
        return cipher ,nonce

    
    def aes_decryption(self,nonce):
        key = encryption.decrypt(self.aes_rsa_key)
        tag = encryption.decrypt(self.encrypted_tag)
        image_bytes = encryption.aes_decrypt(self.bytes,tag,key,nonce)
        return image_bytes
            


if __name__ == "__main__":

    img = ImageObj("image.jpg")
    nonce = img.image_encryption()
    print(img.isEncrypted)
    img.image_decryption(nonce)




