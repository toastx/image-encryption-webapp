import cv2
import numpy as np
import encryption as encryption
import diffie_hellman as dh

class Message():

    def __init__(self):
        self.sender = None
        self.recipient = None
        self.message = None
        self.connection = None

    def create_connection(self,user1, user2):
        connection_key = user1.obj.generate_shared_key(user2.pubkey)
        self.connection = connection_key


class ImageObj():
    def __init__(self,filepath):
        self.image = filepath
        self.isEncrypted = False
        self.encrypted_tag = None
        self.bytes = None
        self.aes_rsa_key = None
        self.encrypted_nonce = None
        
    def image_encryption(self):
        byte_array = self.image_to_bytes(self.image)
        self.aes_encryption(bytes(byte_array))

    def image_decryption(self,nonce):
        if self.isEncrypted:
            image_bytes = self.aes_decryption()
            decoded_image = self.bytes_to_image(image_bytes)
            cv2.imwrite('image_output1.jpg', decoded_image)
            self.encrypted = False
        else:
            print("image not encrypted")
    
    def image_to_bytes(self,image_encrypted):
        file = image_encrypted
        byteArray = np.fromfile(file, dtype=np.uint8)
        return byteArray
    
    def bytes_to_image(self,image_bytes):
        image_byte_array = bytearray(image_bytes)
        np_array = np.asarray(image_byte_array, dtype=np.uint8)
        decoded_image = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)
        return decoded_image

    
    def aes_encryption(self,message):
        cipher, tag, nonce ,key= encryption.aes_encrypt(message)
        aes_rsa_key = encryption.encrypt(key)
        e_tag = encryption.encrypt(tag)
        self.encrypted_tag = e_tag
        self.isEncrypted = True
        self.aes_rsa_key = aes_rsa_key
        self.encrypted_nonce = nonce
        self.bytes = cipher

    def aes_decryption(self):
        key = encryption.decrypt(self.aes_rsa_key)
        tag = encryption.decrypt(self.encrypted_tag)
        nonce = encryption.decrypt(self.encrypted_nonce)
        image_bytes = encryption.aes_decrypt(self.bytes,tag,key,nonce)
        return image_bytes


        




if __name__ == "__main__":

    img = ImageObj("image.jpg")
    nonce = img.image_encryption()
    img.image_decryption(nonce)




