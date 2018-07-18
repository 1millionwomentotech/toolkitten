# 1 Million Women To Tech

## Summer of Code

### Week 1 

### Day 3

#### Love Affair between Numbers and Letters

See love.py

Each string is actually an ordered list of letters. So we can access the first letter by using the so called bracket notation.

The number in the bracket is called the **index** and it starts at zero and grows. Indeces are always integers.

You can also use negative numbers to count down from the end. `-1` will give you the last character in the string.

```python
name = ""
print(name[0])
print(name[-1])
```

This is so powerful because now you can use numbers, calculations, and any kind of arithmetic to access different parts of a string. We will look at a few now. Especially if you use variables as indeces, we can do very nifty things.

It is time to learn how to use the interactive python interpreter on your computer.

Open a new tab in your Command Line and type `python`. You should see `>>>` which means the computer is listening for your python instructions. This is nice for experimenting, just be careful because your code is NOT saved anywhere.

However, when you are testing behaviour of methods, this is a quick way, because you don't have to type print() all the time. The interpreter will implicitly convert your result to a string and print it out for you.

### Mixing It Up 

We’ve looked at a few kinds of objects (integers, floats, and strings), and we made variables point to them. Now it’s time for them all to play nicely together. 

We’ve seen that if we want a program to print 25, the following does not work, because you can’t add numbers and strings together: 

```
var1 = 2
var2 = ​'5'​
print(var1 + var2)
```

Part of the problem is that your computer doesn’t know if you were trying to get `7` (2 + 5) or if you wanted to get `25` ('2' + '5'). But we’ll learn how to do both. 

Before we can add these together, we need some way of getting the string version of var1 or of getting the integer version of var2. 

#### Conversions

To get the string version of an object, we simply use the str() method.

```
var1 = 2
var2 = ​'5'​
print(str(var1) + var2)
25
```

**Vocabulary: programmers will say, we call the str() method on variable var1.**

Similarly, int() gives the integer version of a string literal. float() gives the float version of an integer or string. 

Let’s look at what these  methods do (and don’t do) a little more closely: 

```
var1 = 2
var2 = ​'5'​
print(str(var1) + var2)
print(var1 + int(var2)
print(var1)
print(var2)
25
7
2
5
```

Notice that, even after we got the string version of var1 by calling str(), var1 was always pointing at 2 and never at '2'. 

Unless we explicitly reassign var1 (which requires an = sign), it will point at 2 for the life of the program.

It's time to bite the bullet and look at the official documentation of Python. Note that you can change Language and Version in the top left corner.

To be honest, the official python documentation unfortunately isn't a joy to read but does give one a kind of nerd-satisfaction that only anally retentive documentation can. (Excuse my French.)

#####Reference: 
str():
https://docs.python.org/3/library/stdtypes.html#str

int():
https://docs.python.org/3/library/functions.html#int

float():
https://docs.python.org/3/library/functions.html#float

Python built-in functions:
https://docs.python.org/3/library/functions.html


Try some more interesting (and a few just weird) conversions: 

```
float('15')​
float(99.999'​)
int('99.999'​)

int('5 is my favorite number!'​) 
int('Who asked you about 5 or whatever?'​)
float('Your momma did.'​)

str('stringy'​)
int(3)
```

So, this probably gave you some surprises. 

Explain what happened: what got converted, which parts got ignored. What do the error messages say?

Finally, we saw that our last two conversions did nothing at all, just as we would expect. 

#### Another Look at print()

There’s something strange about our favorite method. Take a look at this: 

```
print(20)
print(str(20))
print(​'20')​
20
20
20
```

Why do these three all print the same thing? Well, the last two should, since `str(20)` is '20'. But what about the first one, the integer 20? For that matter, what does it even mean to write the integer 20? When you write a 2 and then a 0 on a piece of paper, you are writing a string, not an integer. The integer 20 is the number of fingers and toes I have; it isn’t a 2 followed by a 0.

Well, here’s the big secret behind our friend `print()`: before `print()` tries to write out an object, it uses str() to get the string version of that object. 

In fact, in Ruby print() is puts() and the s in puts stands for string; puts really means put string.

This may not seem too exciting now, but Python has many, many kinds of objects (you’ll even learn how to make your own), and it’s nice to know what will happen if you try to print a really weird object, such as a picture of your grandmother or a music file or something. It’ll always be converted to a string first. But that will come later. In the meantime, we have a few more methods for you, and they allow us to write all sorts of fun programs. 

#### The input() Method

If print() means print a string, I’m sure you can guess what input() stands for. And just as print() always spits out strings, input() retrieves only strings. And whence does it get them? 

From you! Well, from your keyboard, anyway. And since your keyboard makes only strings, that works out beautifully. What actually happens is that input() just sits there, reading what you type until you press Enter. 

Let’s try it: 

```
>>>print(input())

  ​Is there an echo in here?​
  Is there an echo in here?
```

Of course, whatever you type will just get repeated back to you. Run it a few times, and try typing different things. 

#### Did It Work?

Maybe you didn’t need any help installing Python, so you skipped Chapter 1. No problem. 

Maybe you’ve done a little programming before, so you skipped Chapter 2. That’s fine. 

The only thing is that you missed some stuff there that you didn’t really need until now. If you haven’t been running your programs from the command line, then you’ll almost certainly have problems with input(), and we’re going to be using it a lot from now on. So, if you saved your program as example.py, you should really run your program by typing `python example.py` into your command line. If you’re having trouble getting around on your command line, check out Chapter 1, ​Getting Started​. 

#### A Few Things to Try

- Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name. 

- Bigger, better favorite number. Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.) 

#### Mind Your Variables

>Skip

When writing a program, I always try to have a good feel for what each variable is pointing to: a number, a string, or whatever. Like in the favorite number program, at some point you’ll have the person’s favorite number as a string, and at another point you’ll have it as an integer. It’s important to keep track of which is which, and you can do this by keeping them in different variables. 

And name the variables so it’s easy to tell what they are at a glance. If I had a variable for someone’s name, I might call it name, and I would just assume it was a string. If I had someone’s age in a variable, I might call it age, and I’d assume it was an integer. So if I needed to have the string version of someone’s age, I’d try to make that obvious by calling it something like age_string or age_as_string. 

I’m not sure you know, but this book started out as an online tutorial. (It was much shorter back then.) I’ve gotten hundreds of emails from people getting stuck. In most of those cases, the problem was a conversion problem. And usually, it was just someone trying to add an integer and a string together. Let’s look at that error a bit more closely:

my_birth_month = ​'August'​
my_birth_day = 3
puts my_birth_month + my_birth_day
example.rb:4:in `+': no implicit conversion of Fixnum into String (TypeError)
 from example.rb:4:in `<main>'
 What is this error telling us? First, what’s a Fixnum? Basically, it’s an integer. For performance reasons, given the way computers are built and such, there are two different classes of integers in Ruby: Fixnums and Bignums. Basically, really big integers are Bignums, and smaller ones are Fixnums. You don’t really need to know this, though; all you need to know is that when you see Fixnum or Bignum, you know it’s an integer. 
 So, it can’t convert an integer into a string. Well, you know it can convert an integer into a string, but it doesn’t want to without your explicit instructions. (Eh…it’s only a computer, after all, and computers aren’t exactly known for their independent thinking and initiative.) Honestly, it’s probably a good thing, because maybe you don’t want to convert the integer into a string, you know? Maybe you want to convert the string into an integer. It’s the whole “2 plus 5 adding up to 7 or 25” problem we covered here. 
 It’s easy to get frustrated when your program has errors. I try not to think of them as errors, though. I try to think of them as the pathetic attempts of a socially inept non-native English speaker (your computer) asking for help. If only your computer were a bit more cultured, it might say something more like, “Excuse me, but I’m unclear as to just one small point…did you want me to convert the integer to a string here, or vice versa? Although it’s probably obvious to any human what you are trying to do, I’m just not that bright.” Then it would laugh nervously. Someday our computers will do just that, but in the meantime, pity the poor fool. 

Reference: 

Python style guides, naming variables:
https://www.python.org/dev/peps/pep-0008/?#id45

my_pet

### More About Methods




#### Fancy String Methods

len()
isalpha()
islower()
lower()

Same reference as before: 
https://docs.python.org/3/library/stdtypes.html#str

#### A Few Things to Try

- Angry boss. Write an angry boss program that rudely asks what you want. Whatever you answer, the angry boss should yell it back to you and then fire you. For example, if you type in I want a raise, it should yell back like this: 

```
WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!
```

- Table of contents. Here’s something for you to do in order to play around more with center, ljust, and rjust: write a program that will display a table of contents so that it looks like this: 

Table of Contents 
 
Chapter 1: Getting Started        page 1
Chapter 2: Numbers                page 9
Chapter 3: Letters                page 13

### Higher Math - Optional


#### More Arithmetic - Optional

**
pow(base, power)
365%7
abs(-7)

#### Random Numbers - Optional

Research how to generate a random number with Python.

oooXXXoo
oooXoXoo
XXXooXoo

#### The Math Object - Optional

https://docs.python.org/3/library/math.html




### Flow Control

#### Comparison

#### Branching

#### Looping

#### A Little Bit of Logic

#### A Few Things to Try




## Submission Guidelines

Create a single file called `soc-wk1-cert-firstname-lastname.py` and send PR to the Gold and VIP private repo.




