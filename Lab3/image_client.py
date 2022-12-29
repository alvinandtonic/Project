
import des
import sys
from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname
from RSA import generate_keypair,encrypt,decrypt
import struct


SERVER_IP    = gethostbyname( 'DE1_SoC' )
PORT_NUMBER = 5000
SIZE = 1024
des_key='secret_k'
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

mySocket = socket( AF_INET, SOCK_DGRAM )
message='hello'

#first generate the keypair
#get these two numbers from the excel file
p=1297273
q=1297651
###################################your code goes here#####################################
public, private = generate_keypair(p, q)
#generate public and private key from the p and q values
#send key

message=('public_key: %d %d' % (public[0], public[1]))
mySocket.sendto(message.encode(),(SERVER_IP,PORT_NUMBER))
#send des_key
mySocket.sendto(message.encode(),(SERVER_IP,PORT_NUMBER))
###################################your code goes here#####################################
des_encoded = [str(encrypt(private, letter)) for letter in des_key]
#encode the DES key with RSA and save in DES_encoded, the value below is just an example
[mySocket.sendto(code.encode(),(SERVER_IP,PORT_NUMBER)) for code in des_encoded]
#read image, encode, send the encoded image binary file
file=open(r'myimage.jpg',"rb") 
data=file.read()
file.close()
###################################your code goes here#####################################
coder = des.des()
r = coder.encrypt(des_key, data, cbc=False)  # encrypted image
#the image is saved in the data parameter, you should encrypt it using des.py
#set cbc to False when performing encryption, you should use the des class
#coder=des.des(), use bytearray to send the encryped image through network
#r_byte is the final value you will send through socket
r_byte=bytearray()
for x in r:
    r_byte += bytes([ord(x)])
    
file = open(r'myimage_encrypted.bin', "wb+")
file.write(r_byte)
file.close()

#send image through socket
mySocket.sendto(bytes(r_byte),(SERVER_IP,PORT_NUMBER))
print('encrypted image sent!')

