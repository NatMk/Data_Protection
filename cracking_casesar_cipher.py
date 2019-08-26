# This is an example of a brute force attack on casesar cipher
# We can decipher it by just trying all the shift values from 0 to 25, and one of them will just be readable.

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

str_in = raw_input("Enter ciphertext: ")

for shift_value in range(26):

    n = len(str_in)
    str_out = ""

    for i in range(n):
        c = str_in[i]
        loc = alpha.find(c)
        newloc = (loc +shift_value)%26
        str_out += alpha[newloc]
    print shift_value,str_out
