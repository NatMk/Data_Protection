# This program will find the two numbers that are close together and used in RSA encryption
from decimal import *
Product_Prime_value = int(raw_input("Enter a Large Value That is a Product of 2 Prime Numbers: "))
global Prime_value1
# Example for Product_Prime_value = 10000000000000000016800000000000000005031
getcontext().prec = 50
n = Decimal(Product_Prime_value).sqrt()
# We can jump back by twos because even numbers are certainly not prime, so we don't need to test the even numbers.

#for p in range(100000000000000000083, 100000000000000000030, -2):
for p in range(n, 100000000000000000030, -2):
    if (Product_Prime_value % p) == 0:
        Prime_value1 = p
    print p, Product_Prime_value % p

print ('The Second Prime Number: %10d' %(Prime_value1))

Prime_value2 = Product_Prime_value/Prime_value1
print ('The Second Prime Number: %10d' %(Prime_value2))

