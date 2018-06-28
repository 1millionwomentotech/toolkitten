print("".join([chr(((ord(i)+2)%122)+96) if i.isalpha() and ((ord(i)+2)%122<97) else chr(ord(i)+2) if i.isalpha() else i for i in input("Enter your string:\n")]))
