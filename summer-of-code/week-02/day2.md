# 1 Million Women To Tech

## Summer of Code

### Week 2 

### Day 2

Let's look at the similarities:
- Numbers to Letters the chr() method
- List of lists
- Continent Counter


#### Numbers to Letters the chr() method

```python
for i in range(65,65+2*26):
    print(i, " stands for ", chr(i))
```

#### Things to try

- There is something small that needs fixing. Can you spot it and fix it? (Hint, we only want A-Z and a-z)

- Make a function that prints A-Z and a-z

- Make a function that asks the user for a message, and turns it into a list of numbers. (It's a cypher ;))

"I LOVE YOU" [ 73, , 76, ...]

Optional: Write a function that does a ceaser cypher (Google), ask the user a number, and shift their message by that number.

#### List of lists

To represent the world in Civilization III (or a chess board, or any board for that matter) we can use a string, a list, or as we will do here a list of lists.

```python
​# "M" is visually more dense than "o".​
M = ​'land'​
o = ​'water'​
world = [[o,o,o,o,o,o,o,o,o,o,o],
 [o,o,o,o,M,M,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,M,M,o],
 [o,o,o,M,o,o,o,o,o,M,o],
 [o,o,o,M,o,M,M,o,o,o,o],
 [o,o,o,o,M,M,M,M,o,o,o],
 [o,o,o,M,M,M,M,M,M,M,o],
 [o,o,o,M,M,o,M,M,M,o,o],
 [o,o,o,o,o,o,M,M,o,o,o],
 [o,M,o,o,o,M,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,o,o,o]]
​# These are just to make the map easier for us to read.​
```

To access a specific element within this we can use bracket notation: world[0][0] to world[10][10].

world[0] read as world-subindex-zero or just world-zero, will read the first element, in this case the first row: [o,o,o,o,o,o,o,o,o,o,o] (all water).

world[0][0] read as world-subindex-zero-subindex-zero or just world-zero-zero, will be the first element of the first row: o.

#### Things to try

- Write a function that prints out all elements of the above board, starting from the first element of the first line, till the end. Each line should be read from beginning to end.
- Now write a function that prints out all elements in reverse.


#### Continent Counter

```python
def​ continent_counter(world, x, y):
    if​ world[y][x] != ​'land'​
 ​   # Either it's water or we already counted it,​
 ​   # but either way, we don't want to count it now.​
 ​   return​ 0
  
    # So first we count this tile...​
    size = 1
    world[y][x] = ​'counted land'​
    # ...then we count all of the neighboring eight tiles​
    # (and, of course, their neighbors by way of the recursion).​
    size = size + continent_counter(world, x-1, y-1)
    size = size + continent_counter(world, x , y-1)
    size = size + continent_counter(world, x+1, y-1)
    size = size + continent_counter(world, x-1, y )
    size = size + continent_counter(world, x+1, y )
    size = size + continent_counter(world, x-1, y+1)
    size = size + continent_counter(world, x , y+1)
    size = size + continent_counter(world, x+1, y+1)
    return size
​
print(continent_counter(world, 5, 5))
```

Drumroll, please...

23

#### Things to try

- There is one small bug in the continent counter above. Can you find it and fix it? (Hint: change the world so that the continent borders the edge)

- Write a function that generates an n x n sized board with either land or water chosen randomly.


#### Optional, Advanced

- Run your continent counter for a 20 x 20 board. How long does it take to run? (If it runs quickly, try 30 x 30 ... 100 x 100 just be aware you might end up in a VERY LOOOONG WAIT) - make sure you know how to break a running program as it may take a long time to complete and you might not have time to wait for it ;)

- Write test coverage in unittest and/or trace for Continent Counter.

