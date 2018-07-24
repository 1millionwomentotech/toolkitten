# 1 Million Women To Tech

## Summer of Code

### Week 1 

### Day 1

This week we are following along "Learn Python the Hard Way" by Zed Shaw and adding the secret sauce of testing to the mix.

Something very cool pointed out by this book is that beginner coders can improve on 3 basic meta-skills that are not about programming _per se_ but are indispensable:

1. Reading and Writing
1. Attention to Detail
1. Spotting Differences

Can you spot the difference?

```python
input = ​''​
​while​ input != ​'bye'​:
  input = input()
​
print(​'Come again soon!')​
```

```python
input = ​''​
​while​ input != ​'bye'​:
input = input()
​
print(​'Come again soon!')​
```

As you study and continue with programming, remember that anything worth doing is difficult at first. Maybe you are the kind of person who is afraid of failure, so you give up at the first sign of difficulty. Maybe you never learned self-discipline, so you can't do anything that's "boring." Maybe you were told that you are "gifted," so you never attempt anything that might make you seem stupid or not a prodigy. Maybe you are competitive and unfairly compare yourself to someone who's been programming for more than 10 or 20 years.

Whatever your reason for wanting to quit, keep at it. Force yourself. If you run into a Study Drill you can't do, or a lesson you just do not understand, then skip it and come back to it later. Just keep going because with programming there's this very odd thing that happens. At first, you will not understand anything. It'll be weird, just like with learning any human language. You will struggle with words and not know what symbols are what, and it'll all be very confusing. Then one day BANG---your brain will snap and you will suddenly "get it." If you keep doing the exercises and keep trying to understand them, you will get it.

#### Do Not Copy-Paste

TYPE each of these exercises in, manually. If you copy and paste, it would be better not to do them. The point of these exercises is to train your hands, your brain, and your mind in how to read, write, and see code. If you copy-paste, you are cheating yourself out of the learning experience.

#### Parallels with Week 1 - Intro to Python

As the body of programming, and that of Python itself is limited, there is a lot of overlap between these first two weeks. This is great because you get to do more exercises, practice more, and see how the same concepts are presented and applied by different people.

Let's look at the similarities:
- Tools
- Data types
- Language basics

**Tools** used in both weeks are the same: a text editor, your terminal (sometimes called the shell, command prompt, command line etc), and python. With these 3 you can program anything in python.

Although it is often not said, having a good grasp of your file manager is helpful too: you need to know where your files are, not only the ones you are writing, but also system files, and python installations. This can be accessed through the terminal, but for beginners it is helpful to visually see the directory and file structure. Ex 0 is a detailed setup chapter.

**Data types** are numbers, strings, booleans and we also saw lists last week. This week we will look into dictionaries and objects more in detail. Functions are a special kind of object because they can do things: they can return values as well as have side-effects on other objects, as well as input and output devices such as your screen. Ex 1 to 12 really work on numbers and strings. Ex 13 to 26 you are introduced to functions and files.

Ex 38 - 42 go over lists and dictionaries and introduce you to more advanced topics such as modules and classes.

**Language basics** remain the same: loops and 'control flow' (if, elif, else that allow you to do branching) are the same, but this second week gives you a lot more detail. Ex. 27-33 give you a lot of detail about branching and logic (and, or)

Towards the end you are creating your first website, writing a game, and have introduced more sophistication into the organization of your code by using Object Oriented practices, automated testing, and Modules.


#### Functions, parameters


```python
input = ​''​
​while​ input != ​'bye'​:
  input = input()
​
print(​'Come again soon!')​
```

#### Testing


#### Reading and writing files


# Things to Try

- Calculate a table for each letter in the alphabet from a-z, and count how many times each letter appears in `alice_in_wonderland.txt` (fancy word for counting stuff is "frequency distribution" - because you are counting the frequency of something)

a: 34,560

b: 5,027

...

z: 893

Store the results in a list of lists:

```python
result = [  
            ["a", 34560], 
            ["b", 5027], 
            ... 
            ["z", 893]
         ]
```

Hint: use python's lower() method to turn all alphabetic letters into small case and count them (so "A" counts towards "a"). 

Hint: Ignore non-alphabetic numbers, you can check with python isalpha() method.

### Optional

- If you have already started Python the Hard Way, please choose 5 exercises and write tests for those in unittest and make them pass. Take your ex.py and your test_ex.py and zip them into a single file to upload for submission via the Helpdesk.

- If you haven't started it and you have the .pdf then start the exercises. e.g. 1 - 10 a day. Please note that exercises differ a lot: some are very short, so you could complete more than one a day. Some of them e.g. ex 37 are very long and have long lists of things to try (almost like a reference) as well as many exercises within them. These longer ones could take several days, if not weeks to complete fully.

Aim to read through about 10 a day, and to complete 1 a day, if you can. You are encouraged to work WITH mentors all the time, if you have access to them in Gold and VIP, and/or to work with each other in pairs or even groups if you are DIYers.


