# 1 Million Women To Tech

## Summer of Code

### Week 1 

### Day 4

### Looping

Often, you’ll want your computer to do the same thing over and over again. After all, that’s what they’re supposed to be good at doing.

When you tell your computer to keep repeating something, you also need to tell it when to stop. Computers never get bored, so if you don’t tell it when to stop, it won’t.

We make sure this doesn’t happen by telling the computer to repeat certain parts of a program while a certain condition is true. It works the way if works: 

```python
input = ​''​
​while​ input != ​'bye'​:
  input = input()
​
print(​'Come again soon!')​
```



#### A Little Bit of Logic

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

```
if b >a:
  print()
elif a == 6:
  print()
elif a == 8:
  print()
elif a == b:
  print()
else:
```

#### A Few Things to Try

- “99 Bottles of Beer on the Wall.” Write a program that prints out the lyrics to that beloved classic, “99 Bottles of Beer on the Wall.” 

- Deaf grandma. Whatever you say to Grandma (whatever you type in), she should respond with this: 
HUH?! SPEAK UP, GIRL!

unless you shout it (type in all capitals). If you shout, she can hear you (or at least she thinks so) and yells back: 

NO, NOT SINCE 1938!

To make your program really believable, have Grandma shout a different year each time, maybe any year at random between 1930 and 1950. (This part is optional and would be much easier if you read the section on Python’s random number generator under the Math Object.) You can’t stop talking to Grandma until you shout BYE. 


- Hint: Try to think about what parts of your program should happen over and over again. All of those should be in your while loop. 

- Hint: People often ask me, “How can I make random give me a number in a range not starting at zero?” But you don’t need it to. Is there something you could do to the number random returns to you? 

- Deaf grandma extended. What if Grandma doesn’t want you to leave? When you shout BYE, she could pretend not to hear you. Change your previous program so that you have to shout BYE three times in a row. Make sure to test your program: if you shout BYE three times but not in a row, you should still be talking to Grandma. 

- Leap years. Write a program that asks for a starting year and an ending year and then puts all the leap years between them (and including them, if they are also leap years). Leap years are years divisible by 4 (like 1984 and 2004). However, years divisible by 100 are not leap years (such as 1800 and 1900) unless they are also divisible by 400 (such as 1600 and 2000, which were in fact leap years). What a mess! 

- Find something today in your life, that is a calculation. Go for a walk, look around the park, try to count something. Anything! And write a program about it. e.g. number of stairs, steps, windows, leaves estimated in the park, kids, dogs, estimate your books by bookshelf, toiletries, wardrobe.

When you finish those, take a break! That was a lot of programming. Congratulations! You’re well on your way. Relax, have a nice day, and continue tomorrow. 


### Lists

#### Loop on lists

#### List comprehension

#### More List Methods

Method  Description

append()  Adds an element at the end of the list

clear() Removes all the elements from the list

copy()  Returns a copy of the list

count() Returns the number of elements with the specified value

extend()  Add the elements of a list (or any iterable), to the end of the current list

index() Returns the index of the first element with the specified value

insert()  Adds an element at the specified position

pop() Removes the element at the specified position

remove()  Removes the first item with the specified value

reverse() Reverses the order of the list

sorted()  Sorts the list and creates a new list without modifying the original

#### A Few Things to Try

- Building and sorting an array. Write the program that asks us to type as many words as we want (one word per line, continuing until we just press Enter on an empty line) and then repeats the words back to us in alphabetical order. Make sure to test your program thoroughly; for example, does hitting Enter on an empty line always exit your program? Even on the first line? And the second? 

Hint: There’s a lovely array method that will give you a sorted version of an array: sorted(). Use it! 

- Table of contents. Write a table of contents program here. Start the program with a list holding all of the information for your table of contents (chapter names, page numbers, and so on). Then print out the information from the list in a beautifully formatted table of contents. Use string formatting such as left align, right align, center.


### Writing Your Own Functions

A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

```python
def say_moo():
  print("moo")

# let's call it
say_moo()
```

#### Function Parameters

Information can be passed to functions as parameter.

Parameters are specified after the function name, inside the parentheses. You can add as many parameters as you want, just separate them with a comma.

```python
def praise(student):
    print(student + " is an amazing Pythonista!")

praise("Katie")
```

The following example shows how to use a default parameter value.

If we call the function without parameter, it uses the default value:

```python
def praise(student = "Melinda"):
    print(student + " is an amazing Pythonista!")

praise()

>>>Melinda is an amazing Pythonista!
```

#### Thing to Try

Write a function that prints out "moo" n times. 

#### Return Values

You may have noticed that some methods give you something back when you call them. For example, we say gets returns a string (the string you typed in), and the + method in 5+3 (which is really 5.+(3)) returns 8. The arithmetic methods for numbers return numbers, and the arithmetic methods for strings return strings. 

It’s important to understand the difference between a method returning a value (returning it to the code that called the method), and your program outputting information to your screen, like print() does, which we call a **side-effect**. Notice that 5+3 returns 8; it does not output 8 (that is, display 8 on your screen). 

So, what does print() return? We never cared before, but let’s look at it now: 

```
a = print('b')
print(a)

None
```

The first print() didn’t seem to return anything, and in a way it didn’t; it returned `None`. Though we didn’t test it, the second print() did, too; print() always returns None. Every method has to return something, even if it’s just the special value `None`. 

Take a quick break, and write a program to find out what say_moo returns. 



#### A Few Things to Try

- Old-school Roman numerals. In the early days of Roman numerals, the Romans didn’t bother with any of this new-fangled subtraction “IX” nonsense. 

No Mylady, it was straight addition, biggest to littlest—so 9 was written “VIIII,” and so on. 

Write a method that when passed an integer between 1 and 3000 (or so) returns a string containing the proper old-school Roman numeral. In other words, old_roman_numeral 4 should return 'IIII'. Make sure to test your method on a bunch of different numbers. 

Hint: Use the integer division and modulus methods.

For reference, these are the values of the letters used: 
I = 1 
V = 5 
X = 10  
L = 50
C = 100 
D = 500 
M = 1000

- “Modern” Roman numerals. Eventually, someone thought it would be terribly clever if putting a smaller number before a larger one meant you had to subtract the smaller one. As a result of this development, you must now suffer. Rewrite your previous method to return the new-style Roman numerals so when someone calls roman_numeral 4, it should return 'IV', 90 should be 'XC' etc.


## Helpful links

Problem solving

- Video: https://www.coursera.org/lecture/duke-programming-web/a-seven-step-approach-to-solving-programming-problems-AEy5M
- Book: The Algorithm Design Manual by Steven S Skiena
- Cheat Sheet: http://adhilton.pratt.duke.edu/sites/adhilton.pratt.duke.edu/files/u37/iticse-7steps.pdf

GitHub

- *THE* Git book: https://git-scm.com/book/en/v2

- How to update via SourceTree: https://stackoverflow.com/questions/13273852/how-do-i-update-my-forked-repo-using-sourcetree

- https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/

- Udacity Git course: https://eu.udacity.com/course/how-to-use-git-and-github--ud775


## Submission Guidelines

Create a single file called `soc-wk1-cert-firstname-lastname.py` and include the whole week's exercises in them. Everything from the 'Things to Try' sections. Optional exercises are, well, optional.

DIY: send PR to toolkitten repo, under https://github.com/1millionwomentotech/toolkitten/tree/master/summer-of-code/week-01/wk1-homework-submission

Gold & VIP: From the Membership area http://memberportal.1millionwomentotech.com/gold-vip-login/ open a Helpdesk ticket. In the 'Department' dropdown choose 'Upload File for Certification' and attach your .py file. ;)
