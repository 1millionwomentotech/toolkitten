#!/ usr/bin/env python3
... for i in range(99,-1,-1):
...     if i==0:
...             print('No more bottles of beer on the wall, no more bottles of beer.\n Go to the store and buy some more.')
...     elif i==1:
...             print('1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, 0 bottles of beer on the wall\n')
...     else:
...             print('{no} bottles of beer on the wall, {no} bottles of beer.\nTake one down and pass it around, {non} bottles of beer on the wall.\n'.format(no=i, non=i-1))

