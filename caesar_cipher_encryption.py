alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

str_in = raw_input("Enter message to encrypt, like HELLO: ")
shift_value = int(raw_input("Enter Shift Value: "))

n = len(str_in)
str_out = ""

for i in range(n):
   c = str_in[i]
   loc = alpha.find(c)
   newloc = (loc + shift_value)%26
   str_out += alpha[newloc]

print "Obfuscated version:", str_out

