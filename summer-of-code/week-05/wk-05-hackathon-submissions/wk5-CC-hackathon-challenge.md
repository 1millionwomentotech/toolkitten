# 1 Million Women To Tech

## Summer of Code

### Week 5 Hackathon Challenge: Continent Counter in JavaScript

Same as Week 1 but in JavaScript.

Task: Calculate the size of a continent you are standing on in your 11 x 11 world in Civilization III.

Bonuses for:
- calculate continent size for all continents in the world
- random world generator
- fastest program
- benchmarking
- extension of the problem to n x n size world

If you are intermediate / advanced try to do your own research about Civilization III and the start working on the above. Submit your program via PR with the following file name:

```
soc05h-cc-firstname-lastname.html
```

Include your JavaScript code as inline JavaScript in a `<script>` tag.

`soc` is for the Summer Of Code
`05`  is for Week 5
`h`   is for hackathon
`cc`  is for Continent Counter
`firstname-lastname` is your name, to make sure there are no clashes with other people's submissions when you send a Pull Request into the same sub-folder.

If you are a beginner or false beginner, read on. We'll be also giving out hints every day.

### Hint 1

When generating the worlds for the game Civilization III, we want worlds
with two primary supercontinents; those tend to be a lot of fun and just sort
of feel “earthy” and... real. 

The process, then, was something like the following:

1. Build the world.
2. Find a "continent" (which could be a one-tile island... at this point we wouldn’t know).
3. Compute its size.
4. Find another continent (making sure not to count any of them twice but
also making sure each gets counted), and repeat the process.
5. Then find the largest two, and see whether they look like fun to play on.

The fun part (actually, it was all fun, not just this part!) was in computing
each continent’s size so that is the challenge for this week's hackathon.

Let’s look at a trimmed-down version. Let’s say we have an 11x11 world
(represented as an array of array... basically just a grid) and that we want to
find the size of the continent in the middle (that is, the continent of which
tile (5,5) is a part). We don't want to count any land tiles belonging to any of
the other continents. Also, as in Civilization III, we'll say that tiles touching
only at the corners are still considered to be on the same continent (since
units could walk along diagonals).

But before you get to the code, solve the problem in English first. It will help.

There are two types of tiles: water and land
We only want to count land
You CAN travel diagonally
[ 0, 1 ]
[ o, X ]
