# 1 Million Women To Tech

## Summer of Code

### Week 2 

### Day 3

Today we will take a big step and learn about dictionaries and classes.

- Dictionaries
- Classes


#### Dictionaries

Yesterday we worked with list of lists to make a board. 

We also used it to count the frequency of each letter in the English alphabet for alice_in_wonderland.txt

```python
frequency_distribution = [
    ["a", 35000],
    ["b", 8000],
    ...
    ["z", 450]
]
```

Today we will look at a new built-in python data type the `dictionary`, which looks like this.

```python
my_dict = {
    "a": 35000,
    "b": 8000,
    "z": 450
}
```

Key-value pairs

- change value
- constructor
- add item
- remove item

When we delete the dictionary, it will cease to exist and **throw** us an error.

```python
Traceback (most recent call last):
  File "day3.py", line 33, in <module>
    print(my_dict)
NameError: name 'my_dict' is not defined
```

Two ways of creating - **instantiating** a dictionary:
- notation {}
- Constructor function


Notation

my_var = {}


Constructor

my_var = dict()


#### Things to try

- Modify "a" for another name in my_dict. Hint: you will have to create a new key-value pair, copy in the value, and then delete the old one.

- Redo the frequency distribution of alice_in_wonderland.txt and save your result in a dictionary.

- Create a dictionary with your own personal details, feel free to be creative and funny so for example, you could include key-value pairs with `quirky fact`, `fav quote`, `pet`. Practice adding, modifying, accesing.

#### Optional / Advanced

Do Python the Hard Way ex. 39 exercises

- Mapping with cities and states/regions in your country or some other country.
- Find the Python documentation for dictionaries and try to do even more things to them.
- Find out what you can't do with dictionaries. A big one is that they do not have order, so try playing with that.

Testing

- Write a test to check the outcome of the alice_in_wonderfland task: one test for list of lists, and one test for dictionary output.


#### Classes

```python
class Student():
    discord_id = ""

s1 = Student()
print(s1.discord_id)
```

The `__init__()` function.

```python
class Student():
    def __init__(self, name, email, dream):
        self.name = name
        self.email = email
        self.dream = dream

s1 = Student("Sandra", "sandra.bullock@email.com", "Support Sudanese women's equality in the home")

print(s1)
print(s1.name)
print(s1.dream)
```

Bottom line: objects are just buckets of key-value pairs

- create object
- initialize
- my_print method: a method is a function that is attached to an object
- self parameter
- modify property
- delete property
- delete object

```
<__main__.Student object at 0x1045ef4e0>
```

#### Things to try

- Review the chat reply of today's beautiful class interaction and instantiate a student variable for everyone who shared their dream.

- Translate the real world 1MWTT student into a Student class, decide on all the attributes that would be meaningful.

Hint: You can start with the DIY signup form https://memberportal.1millionwomentotech.com/diy but feel free to be creative and add/modify as you see it best! This is the REAL work of a creator to find the meaningful description of reality and translate it for computers.

#### Optional, Advanced

Python the Hard Way ex 30 Study Drills

- Write some more songs using this and make sure you understand that you're passing a list of strings as the lyrics.
- Put the lyrics in a separate variable, then pass that variable to the class to use instead.
- See if you can hack on this and make it do more things. Don't worry if you have no idea how, just give it a try, see what happens. Break it, trash it, thrash it, you can't hurt it.
- Search online for "object-oriented programming" and try to overflow your brain with what you read. Don't worry if it makes absolutely no sense to you. Half of that stuff makes no sense to me too.
