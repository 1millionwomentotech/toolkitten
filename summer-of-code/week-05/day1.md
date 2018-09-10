# #1millionwomentotech #SummerOfCode

# Week 5 - Intro to JavaScript

## Day 1

### Getting Started

First ECMAscript specs: 
- https://www.ecma-international.org/publications/files/ECMA-ST-ARCH/ECMA-262,%201st%20edition,%20June%201997.pdf

Published standards:
- http://www.ecma-international.org/publications/standards/Ecma-262-arch.htm 

#### 1 Install Fest 

We'll be using two main tools when we program: a text editor (to write your programs) and the JavaScript console inside your browser (which is how you tell your computer which programs you want to run).

Although there are only a few major browsers, there are many text editors to choose from—and some are much better for programming than others. A good text editor can help catch many of those "stupid mistakes" that beginner programmers make... oh, all right, that all programmers make. 

It makes your code much easier for yourself and others to read in a number of ways: by helping with indentation and formatting, by letting you set markers in your code (so you can easily return to something you are working on), by helping you match up your parentheses, and most important by syntax coloring (coloring different parts of your code with different colors according to their meanings in the program). You’ll see syntax coloring in the examples in this book.

```
Syntax coloring is also called **syntax highlighing**.
```

With so many good editors (and so many bad ones), it can be hard to know which to choose. I'll tell you which one I use, though; that will have to be good enough for now. But whatever you choose as your text editor, do not use a word processor! Aside from being made for an entirely different purpose, they usually don't produce plain text, and your code must be in plain text for your programs to run.

I recommend that you use the Chrome Web Browser because it works on all platforms and because the built-in JavaScript and developer tools are very good.

If you are ready to get started, here are the download and install links:
- [Sublime Text 3](https://www.sublimetext.com/3)
- [Chrome](https://www.google.com/chrome/)


#### 1.1 Running JavaScript

Today we will show you three ways to run JavaScript on your computer.

- in the console
- inline JavaScript (in HTML file)
- source file (in HTML file)

##### In the console:

First, let’s open Chrome and go to View, then Developer, and then to Javascript console.

You can type in calculations and `console.log()` statements directly. 

##### Inline JavaScript:

Open a file and add a `script` tag with JavaScript in the middle.

Save your program (yep, that’s a complete program!) as `day1.html`. Now run your program by opening `day1.html` in your browser. Go and inspect your console. Magic!

See, programming isn’t so hard, now is it?

##### Source file (in HTML file)

It's better to separate HTML and JS files from each other. So we will use a `<script src="yourcooljavascriptfile.js"></script>` tag and add the programs into our cool JavaScript file instead.

Now save both files and open the HTML file again in your browser, and inspect your console. Voila!

#### 2.1 Did It Work?

If it worked, that’s great. But I get a lot of questions from women who are stuck right here. Did you see a window flash up and then disappear? Or nothing at all? If so, the problem is probably that you didn't run your program from the browser.

Don't just click your program's icon.

Don't just press F5 in your text editor.

Run it by opening the `day1.html` file inside the Chrome browser and looking into the console. Trust me.

#### 2.2 Introduction to console.log()

So, what’s going on in that program? 

I’m sure you can guess what the 1+2 does; our program is basically the same as this:

```
console.log(3)
```

`console.log()` simply writes onto the console whatever comes in the brackets after it. If you are running this inside your console, you will also get a **return value** printed, which will be `undefined` by default. Don't worry about that now, we will talk about it again in Day 3.

#### 2.3 Integer and Float

In most programming languages (and JavaScript is no exception), numbers without decimal points are called integers, and numbers with decimal points are usually called floating-point numbers or, more simply, floats.

Here are some integers:

```
5
-205
9999999999999999999999999
0
```

And here are some floats:

```
54.321
0.001
-205.3884
0.0
```

In practice, most programs don’t use floats; they use only integers. (After all, no one wants to look at 7.4 emails, browse 1.8 web pages, or listen to 5.24 of their favorite songs.) 

Floats are used more for academic purposes (physics
experiments and such) and for audio and video (including 3D) programs. 

Even most money programs use integers; they just keep track of the number of pennies!

#### 2.4 Simple Arithmetic

```
print(1+2)
print(2*3)
print(5-8)
print(9/2)

print(5 * (12-8) + -15)
print(98 + (59872 / (13*8)) * -51)

# modulus: gives you the remainder after division
print(10 % 2)

# power and bitshift
# credit: alteredco "mathletes"
print(2**8)
print(1<<9)
```

#### 2.5 A Few Things to Try

Basic Exercises for Certification:

Write a program that tells you the following:

- Hours in a year. How many hours are in a year?
- Minutes in a decade. How many minutes are in a decade?
- Your age in seconds. How many seconds old are you? (I'm not going to check your answer, so be as accurate—or not—as you want.)
- Cristina Tarantino: 32 yesterday! How many milliseconds old is she hahaha? Calculate @Cristina Tarantino's age in milliseconds.

Here are some tougher questions:

- How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
- How about a 64-bit system?
- Calculate your age accurately based on your birthday (maybe use time of day e.g. 8:23am if you know it, use 12:00 noon midday) - you will need JavaScript DateTime functionality.

## Submission Guidelines

Create a single file called `soc-wk5-cert-firstname-lastname.zip` and include the HTML and JS files within. Please submit Gold and VIP support ticket -> Upload File for Certification.


## Reference

MDN (my favourite documentation of all time(!))
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/JavaScript_technologies_overview
