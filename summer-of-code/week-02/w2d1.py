# def moo(n):
# 	return ('moo'*n)

# # moo(0)
# # moo(1)

# for i in range(3):
# 	moo(i)

# filename = "alice_in_wonderland.txt"
# file = open(filename,encoding="utf8")

# # for line in file:
# # 	print(line)

# raw = file.read()
# print(raw[:65])
# print(len(raw))

my_dict = {
	"a" : 5000,
	"b" : 1000,
	"c" : 24
}

print(my_dict)

my_dict["a"] = "yayy"
print(my_dict)

mine = dict(name="hee",age = "34")
print(mine)

my_dict["abc"] = 128
print(my_dict)

del(my_dict["b"])
print(my_dict)

del(my_dict)
print(my_dict)