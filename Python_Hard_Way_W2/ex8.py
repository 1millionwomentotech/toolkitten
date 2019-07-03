formatter = "{} {}  {}  {} " # this is the equivalent of taking a data of type str and creating positions (and blueprints?) for different arguments that will later be passed in and storing it in a variable called 
#formatter

print(formatter.format(1, 2, 3, 4))  #The first argument being passed in and printed is of data type int (1,2,3,4) and they go into the 4 positions set by the {}
print(formatter.format("one", "two", "three", "four")) #The second argument being passed in and printed is of data type str ("one", "two"...) and they go into the 4 positions set by {}
print(formatter.format(True, False, False, True)) #The third argument being passed in and printed is of data type Boolean (True, False, False, True) and they go in the 4 positions set by {}
print(formatter.format(formatter, formatter, formatter, formatter)) #The fourth argument being passed in and printed is of data type var (pointing to a str with 4 {} so this will print 16 of them total)
print(formatter.format(                                              #The fifth argument being passed in is of data type str and there are 4 strings being passed in, 1 string per position or {} and will print a total of 4 distinct {} on same line :)
	"Small are your feet", 
	"And long is the road",
	"Will measures more",
	"Just shut up and code!"
	))



#OK! I think I get what this is doing!



