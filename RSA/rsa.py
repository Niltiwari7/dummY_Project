import random

def gcd(a,b):
    while b!=0:
        a,b = b,a%a
    return a

def isPrime(n,k=5):
    if n<=1 or n==4:
        return False
    if n<=3:
        return True
    d = n - 1
    s = 0
    while d%2==0:
        d//=2
        s+=1

def try_composite(a):
    if pow(a,d,n)==1:
        return False
    for i in range(s):
        if pow(a,2**i*d,n)==n-1:
            return False 
        return True 
    
    for _ in range(k):
        a = random.randrange(2,n-1)
        if try_composite(a):
            return False
    return True 

def generate_large_prime(bit_length):
    while True:
        num = (1<<(bit_length-1))|random.getrandbits(bit_length-1)
        num|=1
        if isPrime(num):
            return num

def multiplicate_inverse(e,phi):
    d=0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi 

    while(e>0):
        temp1 = temp_phi//e
        temp2 = temp_phi-temp1*e
        temp_phi = e
        e = temp2
        x = x2 - temp1*x1
        y = d - temp1*y1
        x2 = x1 
        x1 = x
        d=y1 
        y1 = y

    if temp_phi == 1:
        return d+phi 

def generate_key_pair(p,q):
    if p==q:
        raise ValueError('p and q cannot be equal')
    n = p*q
    phi = (p-1)*(q-1)
    print(f"phi:{phi}")
    e = 65537
    g = gcd(e,phi)
    while g!=1:
        e = random.randrange(1,phi)
        g = gcd(e,phi)
    d = multiplicate_inverse(e,phi)

    return ((e,n),(d,n))

def encrypt(pk,plaintext):
    key,n = pk
    cipher = [pow(ord(char),key,n) for char in plaintext]
    return cipher

def decrypt(pk,ciphertext):
    key,n  = pk
    aux = [str(pow(char,key,n)) for char in ciphertext]
    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)

p  = generate_large_prime(1024)
q = generate_large_prime(1024)
public,private = generate_key_pair(p,q)
message = input()