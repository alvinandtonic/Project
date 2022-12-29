
import random


#fnction for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#uses extened euclidean algorithm to get the d value
#for more info look here: https://crypto.stackexchange.com/questions/5889/calculating-rsa-private-exponent-when-given-public-exponent-and-the-modulus-fact
#will also be explained in class
def get_d(e, z):
    d=0
    init_z = z
    rs = [0, 0]     
    rsL = [1, 0]    
    rsR = [0, 1]    
    while True:
        constant = int(z/e)   
        temp = e
        e = z % e
        z = temp
        rs[0] = rsL[0] - constant*rsR[0]    
        rs[1] = rsL[1] - constant*rsR[1]
        rsL[0] = rsR[0]     
        rsL[1] = rsR[1]
        rsR[0] = rs[0]     
        rsR[1] = rs[1]
        d = rs[1]           
        
        if z % e == 0:      
            break

    while d < 0:
        d = d + init_z

    return d
    
def is_prime (num):
    if num > 1: 
      
        # Iterate from 2 to n / 2  
       for i in range(2, num//2): 
         
           # If num is divisible by any number between  
           # 2 and n / 2, it is not prime  
           if (num % i) == 0: 
               return False 
               break
           else: 
               return True 
  
    else: 
        return False


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p*q
    z = (p-1)*(q-1)
    e = n-1

    while True:
        if gcd(e,z) == 1:
            break
        else:
            e = e-1
            if e < 0:
                print('e cannot not exist')
                break
            d=get_d(e,z)
    return ((e, n), (d, n))

def encrypt(pk, plaintext): 
    m = ord(plaintext)
    e = pk[0]
    n = pk[1]
    cipher = pow(m, e, n)

    return cipher

def decrypt(pk, ciphertext): 
    d = pk[0]
    n = pk[1]
    plain = pow(ciphertext, int(d), int(n))
    plain = chr(plain)

    return plain
