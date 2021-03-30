#!/bin/bash
# This script allows users to encrypt and\or decrypt files based on aes-256-cbc encryption.
echo "Please enter the function you wish to use: 
(1) Encrypt
(2) Decrypt"
read -e option
if [ $option == '1' ]
then
	echo "Please enter the location for the file you wish to encrypt: "
	read -e location
	echo "Where whould you like the file to be saved? "
	read -e destination
	openssl aes-256-cbc -in $location -out $destination	
	echo "File was encrypted successfully"
elif [ $option == '2' ]
then
	echo "Please enter the location of the file you wish to decrypt: "
	read -e location
	echo "Where whould you like the file to be saved?"
	read -e destination
	openssl enc -aes-256-cbc -d -in $location > $destination
	echo "File was decrypted successfuly"
else
	echo "Invalid input"
fi
