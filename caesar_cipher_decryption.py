alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

str_in = raw_input("Enter a cipher text to decrypt like KHOOR: ")
shift_value = int(raw_input("Enter key value: "))

n = len(str_in)
str_out = ""

for i in range(n):
   c = str_in[i]
   loc = alpha.find(c)
   newloc = (loc - shift_value)%26
   str_out += alpha[newloc]

print "Decrypted version:", str_out
