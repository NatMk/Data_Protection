
#!/usr/bin/env python2.7
__author__ = 'ashwini@majestik.net'
'''
	Python functions to simulate Diffe-Hellman key exchange (TLS/SSL handshake),
	for educational use only. 
	This will automatically generate public and private keys, the shared secret, and will check the handshake.
	Does this for 20 cycles, to change edit line 54.
	To change encryption strength edit line 32.
'''
import random

def generatePublicKey(privateKey,prime,base):
	calc1 = base ** privateKey 	# exponent 
	calc2 = calc1 % prime		# modulo
	return calc2

def generateSharedSecret(publicKey,privateKey,prime):
	calc1 = publicKey ** privateKey
	calc2 = calc1 % prime
	return calc2


encryption_strength = 16 	# bits.... 16,32,64,128

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
  101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
   157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 
   223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 
   277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 
   349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 
   419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 
   479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 
   563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 
   619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 
   691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 
   769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 
   853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 
   929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
prime_count = len(prime_numbers)

# let the fun begin

print "\nAlice\t\t\t\tBob\t\t\t\t( {0} bit encryption )".format(encryption_strength)
print "SecretKey\tPublicKey\tSecretKey\tPublicKey\tSharedSecret\tPrime\tBase\n"

funTime = 20
while funTime > 0:
	prime = prime_numbers[random.randrange(prime_count)]
	base = random.getrandbits(encryption_strength)

	alice_secret = random.getrandbits(encryption_strength)
	bob_secret = random.getrandbits(encryption_strength)

	alice_public = generatePublicKey(alice_secret,prime,base)
	bob_public = generatePublicKey(bob_secret,prime,base)

	# these are the same
	alice_shared_secret = generateSharedSecret(bob_public,alice_secret,prime) 
	bob_shared_secret = generateSharedSecret(alice_public,bob_secret,prime)
	
	shared_secret='Do not match'
	if alice_shared_secret == bob_shared_secret: shared_secret=alice_shared_secret

	print '{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}\t\t{5}\t{6}'.format(str(alice_secret),str(alice_public),str(bob_secret),str(bob_public),str(alice_shared_secret),str(prime),str(base))

	funTime = funTime-1

#EOF