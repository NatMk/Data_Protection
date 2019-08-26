text = raw_input ("Enter text: ")
key = raw_input("Enter key: ")
n = len(text)

cipher = ""
for i in range(n):
    t = text[i]
    k = key[i%len(key)]
    x = ord(k) ^ ord(t)
    cipher += chr(x)
print "Plain text: ", text, "Key: ", key, "Cipher text: ", cipher.encode("hex")
