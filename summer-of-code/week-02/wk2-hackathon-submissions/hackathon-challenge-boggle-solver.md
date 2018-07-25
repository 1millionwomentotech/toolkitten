# Week 2 Hackathon challenge

Boggle is a 4x4 word game with 16 dice.

https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Boggle.jpg/220px-Boggle.jpg

After the board is shaken, players have 3 minutes to write down all words they see on the board.

https://ecdn.teacherspayteachers.com/thumbitem/Boggle-Boards-Daily-5-056985700-1372905970-1399574131/original-755526-1.jpg

https://ecdn.teacherspayteachers.com/thumbitem/Boggle-Worksheet-3429774-1507487032/original-3429774-1.jpg

Points are given in the following way:

1 and 2 letter words = 0 points  
3 letter words = 1 point  
4 letter words = 2 points  
5 letter words = 3 points 

(length of the word above 2)

The longest possible word:
16 letter word = 14 points

When you build a word, you can only use one letter once: in other words if you travel along the board and you used a letter, you cannot use it again for the same word, however, you CAN use it for a new word.

You can travel in any direction on the board, diagonal travel is allowed.

The person with the most points win.

Challenge: write a boggle solver that finds all possible words on a given board. You should pick a fixed vocabulary (dictionary): Hasbro standard English dictionary

Bonuses:

- fastest algorithm
- choose dictionary
- choose dice distribution
- extend to 3x3 and 5x5
- benchmark
- What is the MOST number of points possible in boggle? That is, what is the holy grail of Boggle with a fixed dictionary?

# Deadline

Friday of Week 2: 27th of July, 2018 at 9:00am British Time

# Submission guidlines

Your code should return an object in the following format:

```python
result = {
    "score": 143,
    "words": [ "" , "", "", "", ... , ""]
}
```


Where there are two key-value pairs. The first pair has key = "score", and the value should be an integer. The second par has key = "words", and the value should be an alphabetically SORTED list of words.

# Dictionary

https://raw.githubusercontent.com/jonbcard/scrabble-bot/master/src/dictionary.txt

# Dice distribution

Use the ***New Version***:
https://www.boardgamegeek.com/thread/300565/review-boggle-veteran-and-beware-different-version

```
New Version | Old Version  
   AAEEGN   |   AACIOT  
   ELRTTY   |   AHMORS  
   AOOTTW   |   EGKLUY  
   ABBJOO   |   ABILTY  
   EHRTVW   |   ACDEMP  
   CIMOTU   |   EGINTV  
   DISTTY   |   GILRUW  
   EIOSST   |   ELPSTU  
   DELRVY   |   DENOSW  
   ACHOPS   |   ACELRS  
   HIMNQU   |   ABJMOQ  
   EEINSU   |   EEFHIY  
   EEGHNW   |   EHINPS  
   AFFKPS   |   DKNOTU  
   HLNNRZ   |   ADENVZ  
   DEILRX   |   BIFORX  
```



