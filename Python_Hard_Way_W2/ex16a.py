from sys import argv

script, filename = argv

txt = open(filename)

print("Here's the contents of the file I just created with the cow in it.")
print(txt.read())

txt.close()

