# 1 Million Women To Tech

## Summer of Code

### Week 1 

### Day 2

### Letters

We’ve learned all about numbers, but what about letters? Words? Text?

We refer to groups of letters in a program as strings. (You can think of beads with letters on them being strung together.) To make it easier to see just what part of the code is in a string, I’ll color strings `like this`. Here are some strings:

```python
'Hello.'
'Python rocks.'
'Nobody deserves a mime, Buffy.'
'Snoopy says #%^?&*@! when he stubs his toe.'
'     '
''
```

As you can see, strings can have punctuation, digits, symbols, and spaces in them... more than just letters. That last string doesn’t have anything in it at all; we call that an **empty string**.

We used `print()` to print numbers; let’s try it with some strings:

```
print('Hello, world!')
print('')
print('Good-bye.')
```

```
Hello, world!
Good-bye.
```

Dig it.

#### String Arithmetic 

Just as you can do arithmetic on numbers, you can also do arithmetic on strings! Well, sort of... you can add strings, anyway. Let’s try to add two strings and see what `print()` does with that:

```
print('I like' + 'apple pie.')
I likeapple pie.
```

Snap! I forgot to put a space between `I like` and `apple pie.`. 

Spaces don’t usually matter much in your code, but they matter inside strings. (You know what they say: computers don’t do what you want them to do, only what you tell them to do.) 

Take two:

```
print('I like ' + 'apple pie.')
print('I like' + ' apple pie.')
I like apple pie.
I like apple pie.
```

(As you can see, it didn’t matter to which string I added the space.)

So, you can add strings, but you can also multiply them! (And I know you wanted to... you were all like, “But, Ilona, can we multiply them?” Yes. Yes, you can.) Watch this:

```
print('blink ' * 4)
```

And you get this:

```
batting her eyes
```

(Just kidding... not even Python is that clever.)

```
blink blink blink blink
```

If you think about it, this makes perfect sense. After all, 7*3 really just means 7+7+7, so 'moo'*3 just means 'moo'+'moo'+'moo'.

```
>>> 'moo'*3
'moomoomoo'
```

You must think we can now do everything, including division, right?

Let's try it.

```
>>> 'moo'/3
Traceback (most recent call last):
  File "calc.py", line 22, in <module>
    print('moo'/3)
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

No, can no do, I'm afraid.

#### 12 vs. '12'

Before we get any further, we should make sure we understand the difference between numbers and digits. 12 is a number, but '12' is a string of two digits.

Let’s play around with this for a while:
```
print(12 + 12)
print('12' + '12')
print('12 + 12')
24
1212
12 + 12
```

How about this?

```
print(2 * 5)
print('2' * 5)
print('2 * 5')
10
22222
2 * 5
```

These examples are pretty clear. However, if you’re not too careful with how you mix your strings and your numbers, you might run into...

#### Problems

At this point you may have tried some things that didn’t work. If not, here are a few:

```
print('12' + 12)
Traceback (most recent call last):
  File "calc.py", line 32, in <module>
    print('12' + 12)
TypeError: Can't convert 'int' object to str implicitly

print('2' * '5')
Traceback (most recent call last):
  File "calc.py", line 35, in <module>
    print('2' * '5')
TypeError: can't multiply sequence by non-int of type 'str'
```

Hmmm... an error message. The problem is that you can’t really add a number to a string or multiply a string by another string. It doesn’t make any more sense than this does:

```
print('Betty' + 12)
print('Francesca' * 'Hanna')
```

Here’s something else to be aware of: you can write `'pig'*5` in a program, since it just means five sets of the string `'pig'` all added together. However, you can’t write `5*'pig'`, since that means `'pig'` sets of the number 5, which is... poetic, at best.

Finally, what if we want a program to print out `You’re swell!?` We can try this:

```
print('You're swell!')
  File "calc.py", line 40
    print('You're swell!')
                ^
SyntaxError: invalid syntax
```

Well, that won’t work; I can tell that just from the syntax coloring. I won’t even try to run it. The problem is that your computer can’t tell the difference between an apostrophe and a single quote (to end the string). I think the confusion is reasonable here, though. They are the same character, after all.

We need a way to tell the computer “I want an apostrophe here, inside this string.” 

How do we let the computer know we want to stay in the string? We have to **escape** the apostrophe, like this:

```
print('You\'re swell!')
You're swell!
```

**Escaping** special characters

**Escape characters must always escape themselves**. Why?

The backslash is the escape character. In other words, if you have a backslash and another character, they are sometimes translated into a new character.

The only things the backslash escapes, though, are the apostrophe and the backslash itself. (If you think about it, escape characters must always escape themselves, too, to allow for the construction of any string. Why is that?)

Let’s see a few examples of escaping in strings:

```
print('You\'re swell!')
print('backslash at the end of a string: \\')
print('up\\down')
print('up\down')
You're swell!
backslash at the end of a string: \
up\down
up\down
```

Since the backslash does not escape a `d` but does escape itself, those last two strings are identical. Obviously they don’t look the same in the code, but when your program is actually running, those are just two ways of describing identical strings.

You good so far? Good. Let’s start doing something slightly more clever...

### Variables and Assignment

So far, whenever we have printed a string or a number, the thing we printed is gone. What I mean is, if we wanted to print something out twice, we would have to type it in twice:
```
print('...you can say that again...')
print('...you can say that again...')
...you can say that again...
...you can say that again...
```

**Principle: "Don't repeat yourself"**

**Principle: "When coding be lazy. Not just lazy, but agressively, proactively lazy."**

It would be nice if we could just type it in once and then hang on to it... store it somewhere. Well, we can, of course. It would have been insensitive to bring
it up otherwise.

To store the string in your computer’s memory for use later in your program, you need to give the string a name.

Programmers often refer to this process as assignment, and they call the names variables. 

A variable name can usually
be just about any sequence of letters and numbers, but in Python the first character of this name needs to be a lowercase letter. 

Let’s try that last program again, but this time I will give the string the name `my_string` (though I could just as well have named it str or myOwnLittleString or henry_the_8th):

```
my_string = '...you can say that again...'
print(my_string)
print(my_string)
...you can say that again...
...you can say that again...
```


## Few things to try

- Music
- Planets



## Submission Guidelines

Create a single file called `soc-wk1-cert-firstname-lastname.py` and send PR to the Gold and VIP private repo.




