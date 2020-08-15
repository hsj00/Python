# 81, 82 // specific char/str check in string (in)
# 83 check length the string

# 81, 82
msg = input("Type some text: ")
if 'a' in msg:                          # It is able to replace from char to str.
    print("'a' is in the text.")
else:
    print("'a' is not in the text.")

# 83

msg = input("Type some text: ")
msglen = len(msg)
en_msglen = len(msg.encode())
print("Length that you type is <%d>" % msglen)
print("Byte length that you type is <%d>" % en_msglen)
