
# coding: utf-8

# In[2]:


# Boggle solver game
f=open('hasbro.txt','r')                                          # Hasbro standard dictionary has been used
keys=f.read().split("\n")                    
class TrieNode:                                                   # dictionary has been stored in trie data structure to optimize word search speed
    def __init__(self):
        self.children = [None]*26
 
        self.isEndOfWord = False

class Trie:
    def __init__(self):                                           # Trie data structure class
        self.root = self.getNode()

    def getNode(self):                                            # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self,ch):                                    # Converts key current character into index
        return ord(ch)-ord('A')                                   #use only 'A' through 'Z' and upper case
   
    def insert(self,key):  
        pCrawl = self.root                                          # If not present, inserts key into trie
        length = len(key)                                           # If the key is prefix of trie node, 
                                                                    # just marks leaf node where leaf node indicates the end of word
        for level in range(length):
            index = self._charToIndex(key[level])

            if not pCrawl.children[index]:                         # if current character is not present
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        pCrawl.isEndOfWord = True                                  # mark last node as leaf(end of word)
        
    
    
    def isSafe(self,i,j,vis):
        return(i>=0 and i<4 and j>=0 and j<4 and not vis[i][j])     
   
    def search(self,root,boggle,i,j,vis,string):                    #function to search word in boggle by traversing all possible paths
        
        pCrawl =root
        if pCrawl.isEndOfWord ==True:
            if(len(string))>=3:
                max_words.append(string)                            # to make a list of maximum possible words in boggle at a particular shuffle
            
        if t.isSafe(i,j,vis):
            vis[i][j]=True
        
            for k in range(26):
                if pCrawl.children[k] !=None:
                    
                    ch =chr(k+ord('A'))
                    
                    if t.isSafe(i+1,j+1,vis)and boggle[i+1][j+1]==ch:
                        t.search(pCrawl.children[k],boggle,i+1,j+1,vis,string+ch)      #recursive function calls so that all adjacent cells of a particular node are covered
                       
                    if t.isSafe(i,j+1,vis) and boggle[i][j+1]==ch:
                        t.search(pCrawl.children[k],boggle,i,j+1,vis,string+ch)
                        
                    if t.isSafe(i-1,j+1,vis) and boggle[i-1][j+1]==ch:
                        t.search(pCrawl.children[k],boggle,i-1,j+1,vis,string+ch)
                        
                    if t.isSafe(i+1,j,vis) and boggle[i+1][j]==ch:
                        t.search(pCrawl.children[k],boggle,i+1,j,vis,string+ch)
                        
                    if t.isSafe(i+1,j-1,vis) and boggle[i+1][j-1]==ch:
                        t.search(pCrawl.children[k],boggle,i+1,j-1,vis,string+ch)
                      
                    if t.isSafe(i,j-1,vis) and boggle[i][j-1]==ch:
                        t.search(pCrawl.children[k],boggle,i,j-1,vis,string+ch)
                        
                    if t.isSafe(i-1,j-1,vis) and boggle[i-1][j-1]==ch:
                        t.search(pCrawl.children[k],boggle,i-1,j-1,vis,string+ch)
                       
                    if t.isSafe(i-1,j,vis)and boggle[i-1][j]==ch:
                        t.search(pCrawl.children[k],boggle,i-1,j,vis,string+ch)
                       
            vis[i][j]=False
       
  
    import numpy
    def findWords(self,boggle):                       # function to find valid words in boggle by comparing them with words in a fixed dictionary
    
        t=Trie()                                      # t is the instance of Trie data structure 
        vis=[False]*4                                 # vis is a matrix that has all values false initially 
        for i in range(4):                            # vis matrix has been created to improve backtracking that is to ensure that a letter doesn't get repeated in a single word
            vis[i]=[False]*4
        pCrawl=self.root

        string=""
        for i in range(4):
            for j in range(4):
                if pCrawl.children[self._charToIndex(boggle[i][j])]:
                    string=string+boggle[i][j]
                    t.search(pCrawl.children[self._charToIndex(boggle[i][j])], boggle,i,j,vis,string)#
                    string=""


import random
import numpy
from string import ascii_uppercase
data=['']*4
for i in range(4):
    data[i]=['']*4
grid={(0, 0): 'AAEEGN', (0, 1): 'ELRTTY', (0, 2): 'AOOTTW', (0, 3): 'ABBJOO', (1, 0): 'EHRTVW', (1, 1): 'CIMOTU', (1, 2): 'DISTTY', (1, 3): 'EIOSST', (2, 0): 'DELRVY', (2, 1): 'ACHOPS', (2, 2): 'HIMNQU', (2, 3): 'EEINSU', (3, 0): 'EEGHNW', (3, 1): 'AFFKPS', (3, 2): 'HLNNRZ', (3, 3): 'DEILRX'}
for x in range(4):
        for y in range(4):
            data[x][y]=random.choice(list(grid[x,y]))

alphabet=numpy.array(data)
shape=(4,4)
boggle=alphabet.reshape(shape)                           # the grid dictionary helps represent each of the 16 elements of boggle matrix as 16 dice  
                                                         # the bogggle size can be adjusted to 3x3 or 5x5 size board by adjusting the grid elements according to indices of a 3x3 and 5x5 matrix


t=Trie()
for key in keys:
    t.insert(key)  


    
user_words=[]                                           #list to store words entered by user
score=0
def calcScore(word):                                    # function to calculate score of player
    global score
    if word in max_words:
        if word not in user_words:
            if len(word)<3:
                score+=0
            elif len(word)==3:
                score+=1
            elif len(word)==4:
                score+=2
            elif len(word)==5:
                score+=3
            elif len(word)==6:
                score+=4
            elif len(word)==7:
                score+=5
            elif len(word)==8:
                score+=6
            elif len(word)==9:
                score+=7
            elif len(word)==10:
                score+=8
            elif len(word)==11:
                score+=9
            elif len(word)==12:
                score+=10
            elif len(word)==13:
                score+=11
            elif len(word)==14:
                score+=12
            elif len(word)==15:
                score+=13
            elif len(word)==16:
                score+=14
            user_words.append(word)

def game():                                             #function to set 3 minutes timer for player to think and enter input
    import time

    t_end = time.time() + 60 * 3
    while time.time() < t_end:
        word=input().upper()
        calcScore(word)
  

 
if __name__ == '__main__':                              #main function 
    max_words=[]
    print('Welcome! You have 3 minutes of time to think and enter your inputs.')
    print(boggle)
    t.findWords(boggle)
    game()
    
    sorted(user_words)
    result={"score":score,"words":user_words}
    print('Sorry, the time is over!')
    print('Your result is:')
    print(result)                                      # the result is a dictionary which has two keys :one for the score of the user and the other for the list of valid words that he/she entered
    print('The maximum possible words for this shuffle,in case you wanted to know are:')
    print(max_words)
    print('So there were in total',len(max_words),'words possible for this case!')
        


# In[ ]:





# In[ ]:




