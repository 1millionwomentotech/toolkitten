## Exemple

Civilization III is a game of building worlds. It provides a
of the world and divides it into blocks, forming a matrix.
Each of these blocks may contain EARTH or WATER. In blocks of EARTH, it is possible
floor. In those of WATER, no.
Objective: To count the "moveable" blocks of a continent starting from a cen-
and going toward the edges in the eight possible directions.

```python
L = 'terra'
W = 'agua'
```

To compare two continents, it is necessary to have a concrete representation of
both. Let us imagine that these representations are the two arrays,
below.

```python
continent_1 = [
    [W,W,W,W,W,W,W,W,W,W,W],
    [W,L,W,W,W,W,W,W,W,W,W],
    [W,L,L,L,W,W,W,L,W,W,W],
    [W,W,W,L,W,W,W,L,W,W,W],
    [W,W,W,L,W,W,L,W,W,W,W],
    [W,W,W,L,L,L,L,L,W,W,W],
    [W,W,W,L,L,L,L,L,W,W,W],
    [W,W,W,W,W,W,W,L,W,W,W],
    [W,W,W,W,W,W,W,L,W,W,W],
    [W,W,W,W,W,W,W,L,L,L,W],
    [W,W,W,W,W,W,W,W,W,W,W],
]

continent_2 = [
    [W,W,W,W,W,W,W,W,W,W,W],
    [W,L,W,W,W,W,W,W,W,W,W],
    [W,L,L,L,W,W,W,L,W,W,W],
    [W,L,W,L,W,W,W,L,W,W,W],
    [W,L,W,L,W,W,L,W,W,W,W],
    [W,L,W,L,L,L,L,L,W,W,W],
    [W,L,W,L,W,L,L,L,W,W,W],
    [W,W,W,L,W,W,L,W,W,W,W],
    [W,W,W,L,W,W,L,L,W,W,W],
    [W,W,W,W,W,W,L,L,L,L,W],
    [W,W,W,W,W,W,W,W,W,W,W],
]
```

Let's then define how the count will be done.
For this, we must inject the continent together of the initial position of the matrix
proposed by the financial year.

View the result, starting from the central position of the matrix (5, 5), according to
proposed by the exercise.

```python
>>> print('Blocks in continent 1:', cont_blocks_processed(continent_1, 5, 5))
>>> print('Blocks in continent 2:', cont_blocks_processed(continent_2, 5, 5))

Blocks in continent 1: 24
Blocks in continent 2: 31
```