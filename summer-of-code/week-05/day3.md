# 1 Million Women To Tech

## Summer of Code

### Week 5 

### Day 3

#### Love Affair between Numbers and Letters

See love.js

Each string is actually an ordered list of letters. So we can access the first letter by using the so called bracket notation.

The number in the bracket is called the **index** and it starts at zero and grows. Indeces are always integers.

You cannot  use negative numbers to count down from the end. `-1` will give you undefined.

```
    name = ""
    console.log(name[0])
    console.log(name[1])

    // legal in Python, illegal in JavaScript
    console.log(name[-1])
```

This is so powerful because now you can use numbers, calculations, and any kind of arithmetic to access different parts of a string. We will look at a few now. Especially if you use variables as indeces, we can do very nifty things.

It is time to learn how to use the interactive JavaScript interpreter on your computer.

Open a new tab in your Chrome browser and open the JavaScript console. You should see `>` which means the computer is listening for your JavaScript instructions. This is nice for experimenting, just be careful because your code is NOT saved anywhere.

However, when you are testing behaviour of methods, this is a quick way, because you don't have to type console.log() all the time. The interpreter will implicitly convert your result to a string and console.log it out for you.

```
    name. // see there are many methods available to you
    name.toUpperCase()
    name.slice(0,3)
    name.slice(0,-1)

    a = 3
    name.slice(0,a)
    name.slice(a,-1)
    name.slice(a)
    name // strings are **immutable** they cannot be changed
```

### Mixing It Up 

We'​ve looked at a few kinds of objects (integers, floats, and strings), and we made variables point to them. Now it’s time for them all to play nicely together. 

We'​ve seen that if we want a program to console.log 25, the following does work, because the `+` operator converts both sides to a string before adding them together. This is called **implicit** type conversion.

Note: In Python you can'​t add numbers and strings together, you will get an error message about being naughty with your types.

```
    var1 = 2
    var2 = ​'5'​
    console.log(var1 + var2)
```

Part of the problem is that however, that your computer doesn’t know if you were trying to get `7` (2 + 5) or if you wanted to get `25` ('2' + '5'). It just assumed the latter. But we’ll learn how to do both. 

Before we can add these together, we need some way of getting the string version of var1 or of getting the integer version of var2. 

#### Conversions

To get the string version of an object, we simply use the String() method.

```
    var1 = 2
    var2 = ​'5'​
    console.log(String(var1) + var2)
    // > 25
```

**Vocabulary: programmers will say, we call the String() method on variable var1.**

Note, you get this for "free" in JavaScript without having to call the String() method when using the `+` operator.

Similarly, parseInt() gives the integer version of a string literal. parseFloat() gives the float version of an integer or string. 

Let’s look at what these  methods do (and don’t do) a little more closely: 


```
    var1 = 2
    var2 = ​'5'​
    console.log(String(var1) + var2)
    console.log(var1 + parseInt(var2)
    console.log(var1)
    console.log(var2)
    25
    7
    2
    5
```

Notice that, even after we got the string version of var1 by calling String(), var1 was always pointing at 2 and never at '2'. 

Unless we explicitly reassign var1 (which requires an = sign), it will point at 2 for the life of the program.

It's time to bite the bullet and look at the official documentation of JavaScript. Note that you can change Language and Version in the top left corner.

MDN documentation for JavaScript IS a real joy to read. Finally, a documentation that is readable, usable, and fun.

#####Reference: 

slice():
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice


Try some more interesting (and a few just weird) conversions: 

```
parseFloat('15')​
parseFloat(99.999'​)
parseInt('99.999'​)

parseInt('5 is my favorite number!'​) 
parseInt('Who asked you about 5 or whatever?'​)
parseFloat('Your momma did.'​)

String('stringy'​)
parseInt(3)
```

So, this probably gave you some surprises. 

Explain what happened: what got converted, which parts got ignored. What do the error messages say, if anything?

Finally, we saw that our last two conversions did nothing at all, just as we would expect. 

#### Another Look at console.log()

There’s something strange about our favorite method. Take a look at this: 

```
console.log(20)
console.log(String(20))
console.log(​'20')​
20
20
20
```

Why do these three all console.log the same thing? Well, the last two should, since `String(20)` is '20'. But what about the first one, the integer 20? For that matter, what does it even mean to write the integer 20? When you write a 2 and then a 0 on a piece of paper, you are writing a string, not an integer. The integer 20 is the number of fingers and toes I have; it isn’t a 2 followed by a 0.

Well, here’s the big secret behind our friend `console.log()`: before `console.log()` tries to write out an object, it uses String() to get the string version of that object. 

In fact, in Ruby console.log() is puts() and the s in puts stands for string; puts really means put string.

This may not seem too exciting now, but JavaScript has many, many kinds of objects (you’ll even learn how to make your own), and it’s nice to know what will happen if you try to console.log a really weird object, such as a picture of your grandmother or a music file or something. It’ll always be converted to a string first. But that will come later. In the meantime, we have a few more methods for you, and they allow us to write all sorts of fun programs. 

#### The prompt() Method

If console.log() means console.log a string, I’m sure you can guess what input() stands for. And just as console.log() always spits out strings, prompt() retrieves only strings. And whence does it get them? 

From you! Well, from your keyboard, anyway. And since your keyboard makes only strings, that works out beautifully. What actually happens is that prompt() just sits there, reading what you type until you press Enter. 

Let’s try it: 

```
>>>console.log(prompt())

  ​Is there an echo in here?​
  Is there an echo in here?
```

Of course, whatever you type will just get repeated back to you. Run it a few times, and try typing different things. 

#### Did It Work?

Maybe you didn’t need any help installing JavaScript, so you skipped Chapter 1. No problem. 

Maybe you’ve done a little programming before, so you skipped Chapter 2. That’s fine. 

The only thing is that you missed some stuff there that you didn’t really need until now. If you haven’t been running your programs from the console, then you’ll almost certainly have problems with prompt(), and we’re going to be using it a lot from now on. So, if you saved your program as example.py, you should really run your program by opening day1.html in your browser. If you’re having trouble getting around on your console, check out day 1, ​Getting Started​. 

#### A Few Things to Try

- Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name. 

- Bigger, better favorite number. Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.) 

#### Mind Your Variables

When writing a program, I always try to have a good feel for what each variable is pointing to: a number, a string, or whatever. Like in the favorite number program, at some point you’ll have the person’s favorite number as a string, and at another point you’ll have it as an integer. It’s important to keep track of which is which, and you can do this by keeping them in different variables. 

And name the variables so it’s easy to tell what they are at a glance. If I had a variable for someone’s name, I might call it name, and I would just assume it was a string. If I had someone’s age in a variable, I might call it age, and I’d assume it was an integer. So if I needed to have the string version of someone’s age, I’d try to make that obvious by calling it something like `age_string` or `age_as_string`. 

It’s easy to get frustrated when your program has errors. I try not to think of them as errors, though. I try to think of them as the pathetic attempts of a socially inept non-native English speaker (your computer) asking for help. If only your computer were a bit more cultured, it might say something more like, “Excuse me, but I’m unclear as to just one small point... did you want me to convert the integer to a string here, or vice versa? Although it’s probably obvious to any human what you are trying to do, I’m just not that bright.” Then it would laugh nervously. Someday our computers will do just that, but in the meantime, pity the poor fool. 

Reference: 

JavaScript style guides, naming variables:
https://www.JavaScript.org/dev/peps/pep-0008/?#id45

Recommended naming is with capitalized letters, except the first one which is small `myPet`. This is called camelCase and is a convention among JavaScript developers.

### More About Methods

How many methods have you seen in this course so far?

#### Fancy String Methods

length()
toUpperCase()
toLowerCase()

Check out more fancy string methods here: 
https://www.w3schools.com/jsref/jsref_obj_string.asp

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

Optional: in JS we may prefer to 'print' these to the HTML file itself rather than the console.

### Higher Math - Optional

#### More Arithmetic - Optional

**
pow(base, power)
365%7
abs(-7)

#### Random Numbers - Optional

Research how to generate a random number with JavaScript.
(Math.random() will output a random number from 0 up to but not including 1)

- Generate a random number 
    - between 1 and 10
    - between 1 and 100
    - between 1930 and 1950

Optional:

Then try to generate your random Civilization III world by generating a land 'X' tile or a water 'o' tile randomly:

- oooXXXoo
- oooXoXoo
- XXXooXoo

#### The Math Object - Optional

https://www.w3schools.com/jsref/jsref_obj_string.asp


## Helpful links

Problem solving

- Video: https://www.coursera.org/lecture/duke-programming-web/a-seven-step-approach-to-solving-programming-problems-AEy5M
- https://github.com/gwhorleyGH/java-coursera/wiki/Seven-step-approach-to-solving-programming-problems
- Book: The Algorithm Design Manual by Steven S Skiena

Fun video about type conversion
- https://www.destroyallsoftware.com/talks/wat

Cool in-depth article about JavaScript type coercion
- https://medium.freecodecamp.org/js-type-coercion-explained-27ba3d9a2839

