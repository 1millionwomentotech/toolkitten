# 1 Million Women To Tech

## Summer of Code

### Week 1 

### Day 1

### Install Fest

Well be using three main tools when we program: a text editor (to write your programs), the Python interpreter (to run your programs), and your command line (which is how you tell your computer which programs you want to run).

Although there’s pretty much just one Python interpreter and one command line, there are many text editors to choose from—and some are much better for programming than others. A good text editor can help catch many of those "stupid mistakes" that beginner programmers make... oh, all right, that all programmers make. 

It makes your code much easier for yourself and others to read in a number of ways: by helping with indentation and formatting, by letting you set markers in your code (so you can easily return to something you are working on), by helping you match up your parentheses, and most important by syntax coloring (coloring different parts of your code with different colors according to their meanings in the program). You’ll see syntax coloring in the examples in this book.

```
Syntax coloring is also called **syntax highlighing**.
```

With so many good editors (and so many bad ones), it can be hard to know which to choose. I'll tell you which one I use, though; that will have to be good enough for now. But whatever you choose as your text editor, do not use a word processor! Aside from being made for an entirely different purpose, they usually don't produce plain text, and your code must be in plain text for your programs to run.

Since setting up your environment differs somewhat from platform to platform (which text editors are available, how to install Python, how your command line works...), we’ll look at setting up each platform covered in this course, one at a time.

If you are ready to get started, here are the download and install links:
- [Sublime Text 3](https://www.sublimetext.com/3)
- [Python 3.7.0](https://wiki.python.org/moin/BeginnersGuide/Download)


#### 1.1 Windows 

First, let’s install Python. Go get the One-Click Installer from the website [https://wiki.python.org/moin/BeginnersGuide/Download](https://wiki.python.org/moin/BeginnersGuide/Download) by clicking Download and then clicking the highest-numbered version of Python you see there (version 3.7.0 as of this writing). When you run it, it will ask you where you want to install Python and which parts of it you want installed. Just accept all the defaults.

Now let’s make a folder on your desktop in which you’ll keep all of your programs.

Right-click your desktop, select New, and then select Folder. Name it something truly memorable, such as `programs`. Now double-click the folder to open it.

To make a blank Python program, right-click in the folder, select New, and then select Text Document. Rename the document to have the `.py` file extension.

So if it was "New Text Document.txt", rename it to "ponies.py" (if your program was about ponies).

Now you need a text editor. I am a fan of [Sublime Text 3](https://www.sublimetext.com/3), so unless you already have a favorite text editor, go ahead and download and install that one.

To actually run your programs, you’ll need to go to your command line. In your Start menu, select Accessories, and then choose Command Prompt.

You’ll see something like this:

```
Microsoft Windows XP [Version 5.1.2600]
(C) Copyright 1985-2001 Microsoft Corp.

C:\Documents and Settings\ilonabudapesti>_
```

#### 1.2 Mac OS X 

Demo

Sublime

Command + N

Optional for Mac, you can use the built-in command prompt or what I use
- [iTerm2](https://www.iterm2.com/index.html) - Mac

#### 1.3 Linux 

Links


### 2 Numbers

Now that you’ve gotten everything ready, it’s time to write your first program!

Open your text editor, and type the following:
```
print(1+2)
```

Save your program (yep, that’s a complete program!) as `calc.py`. Now run your program by typing ruby `calc.py` into your command line. 

It should put a 3 on your screen. 

See, programming isn’t so hard, now is it?

#### 2.1 Did It Work?

If it worked, that’s great. But I get a lot of questions from women who are stuck
right here. Did you see a window flash up and then disappear? Or nothing
at all? If so, the problem is probably that you didn’t run your program from
the command line.

Don’t just click your program’s icon.

Don’t just press F5 in your text editor.

Run it by typing `python calc.py` into your command line. Trust me.

#### 2.2 Introduction to print()

So, what’s going on in that program? 

I’m sure you can guess what the 1+2 does; our program is basically the same as this:
```python
print(3)
```

`print()` simply writes onto the screen whatever comes in the brackets after it.

#### 2.3 Integer and Float

In most programming languages (and Python is no exception), numbers without decimal points are called integers, and numbers with decimal points are usually called floating-point numbers or, more simply, floats.

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

```python
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
- Andreea Visanoiu​: I'm 48618000 seconds old hahaha. Calculate @Andreea Visanoiu's age.

Here are some tougher questions:

- How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
- How about a 64-bit system?
- Calculate your age accurately based on your birthday (maybe use time of day e.g. 8:23am if you know it, use 12:00 noon midday) - you will need Python modules.

## Submission Guidelines

Create a single file called `soc-wk1-cert-firstname-lastname.py` and send PR to the Gold and VIP private repo.

