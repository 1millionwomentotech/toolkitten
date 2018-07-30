#This is the code to generate the legal moves in Boggle for each length of word.

#The rules of Boggle dictate that when creating a word you can start from any die but the next choice must
#be directly adajcent vertically, horizontally or diagonally. For each word, each next die chosen must follow this rule
#and have not already been used for that word.

#To create lists of all permutations of 3, 4, 5 die combinations etc. (up to 16) without taking the rules into account
#requires too much memory to calculate. The number of 16 die possibilities are 20,922,789,888,000! This is larger than the maximun
#number of elements a list can contain in Python (536,870,912). Even discarding combinations that are not possible within the
#rules it still generates an encourmous amount of data. It takes around an hour to generate the permutations and they cannot
#be stored in a single list because of memory capacity when generating each one. 

#As the legal moves will remain the same for any 4x4 Boggle Board I decided to store the legal moves in pickle files
#that can be called into the eventual Boggle Solver. This means I only need to generate the data once for multiple uses.
#Given the capacity of memory I have had to split the generation of the list into 6 seperate files.

#One thing to note is the method for generating permutations. As mentioned generating permutations for larger die combinations
#(generally 6 or more) required so much memory and took very long to do. As a result I decided not to generate all permutations
#and discard 'illegal' moves as I went. Instead I used the methods to produce 3 and 4 die combinations and extended them by
#finding all the 3 or 4 dice combinations that started with the same die that they ended withand, providing the two didn't
#contain any repetitions would append them together (removing the first die location of the second set of dice options). I would
#then repeat this as necessary to generate the correct number of die combinations. My reasoning for this methodology is that
#with the 3 and 4 dice combinations I could already be certain that they already had only legal combinations based on boggle rules.
#This meant that I would not have to check each die choice individually to check they produced a legal move.


#Libraries
#Importing in tools for creating permutations quickly, timing the program and pickling the lists for reuse
import itertools
from timeit import default_timer as timer
import pickle


#Creates the grid coordinates for the die
def gridLocations(a,b):
    global all_locations
    all_locations = [(x,y) for x in range(a) for y in range(b)]


#Works out the coordinates adjacent to the chosen coordinate to assist with choosing legal moves in the game
def possibleLocations(i,j):
    possibleLocations = set()
    for y in range(i-1, i+2):
        for z in range(j-1, j+2):
            location = (y,z)
            possibleLocations.add(location)
    return possibleLocations


#Generates 3 dice possibibilies, weeding out any combinations that don't meet the rules of selection
def combos3():
    global boggle_board, three_combos
    choice = all_locations[:]
    three_combos = []
    for permutation in map(list, itertools.permutations(choice,3)):
        for c in range(len(permutation)-1):
            nextMoves = possibleLocations(permutation[c][0], permutation[c][1])
            to_check = set()
            to_check.add(permutation[c+1])
            if to_check.issubset(nextMoves) == True:
                if c < (len(permutation)-2):
                    c+=1
                else:
                    three_combos.append(permutation) 
            else:
                break
    return three_combos


#Generates 4 dice possibibilies, weeding out any combinations that don't meet the rules of selection
def combos4():
    global boggle_board, four_combos, final4
    choice = all_locations[:]
    four_combos = []
    for permutation in map(list, itertools.permutations(choice,4)):
        for c in range(len(permutation)-1):
            nextMoves = possibleLocations(permutation[c][0], permutation[c][1])
            to_check = set()
            to_check.add(permutation[c+1])
            if to_check.issubset(nextMoves) == True:
                if c < (len(permutation)-2):
                    c+=1
                else:
                    four_combos.append(permutation) 
            else:
                break
    return four_combos


#The function that enables 3 dice combinations to be appended to all the possible combinations already generated
def append3():
    global mixCombos
    combos3()
    amended_list = []
    for i in range(len(mixCombos)):
        to_check = mixCombos[i]
        for j in range(len(three_combos)):
            secondList = three_combos[j]
            last = to_check[len(to_check)-1]
            first = secondList[0]
            if last == first :
                combined = set(secondList[1:]).intersection(set(to_check))
                if len(combined) <1:
                    to_add = secondList[1:]
                    new_word = to_check + to_add
                    amended_list.append(new_word)
    mixCombos = amended_list[:]


#The function that enables 4 dice combinations to be appended to all the possible combinations already generated
def append4():
    global mixCombos
    combos4()
    amended_list = []
    for i in range(len(mixCombos)):
        to_check = mixCombos[i]
        for j in range(len(four_combos)):
            secondList = four_combos[j]
            last = to_check[len(to_check)-1]
            first = secondList[0]
            if last == first :
                combined = set(secondList[1:]).intersection(set(to_check))
                if len(combined) <1:
                    to_add = secondList[1:]
                    new_word = to_check + to_add
                    amended_list.append(new_word)
    mixCombos = amended_list[:]


#The function that generates the base case of combinations to be extended and controls the calling of the append functions
def multiCombos(a,b):
    global mixCombos, final_words, amended_list
    combos3()
    combos4()
    if a > 0:
        mixCombos = four_combos[:]
    else:
        mixCombos = three_combos[:]
    countFour = a - 1
    countThree = b
    for i in range(countFour):
        append4()
    for j in range(countThree):
        append3()
  


#generates the dice combinations for words between 3 and 10 letters in length
def words_length3to10():
    timer1 = timer()
    gridLocations(4,4)
    all_combos = []
    all_combos2 = []
    combinations = [[0,2],[1,1],[2,0],[1,2],[2,1],[3,0]]
    combos3()
    all_combos = all_combos + three_combos
    combos4()
    all_combos = all_combos+four_combos
    for item in combinations:
        multiCombos(item[0], item[1])
        all_combos = all_combos + mixCombos
    pickle.dump(all_combos,open("legalCombinations1.p", "wb"))
    timer2 = timer()
    print('The total number of combinations =', len(all_combos))
    print('Time taken to achieve=', timer2-timer1)
    


#generates the dice combinations for words of 11 letters in length
def words_length11():
    timer1 = timer()
    gridLocations(4,4)
    all_combos = []
    multiCombos(2, 2)
    all_combos = all_combos + mixCombos
    pickle.dump(all_combos,open("legalCombinations2.p", "wb"))
    timer2 = timer()
    print('The total number of combinations =', len(all_combos))
    print('Time taken to achieve=', timer2-timer1)


 
 #generates the dice combinations for words of 12 letters in length
def words_length12():
    timer1 = timer()
    gridLocations(4,4)
    all_combos = []
    multiCombos(3, 1)
    all_combos = all_combos + mixCombos
    pickle.dump(all_combos,open("legalCombinations3.p", "wb"))
    timer2 = timer()
    print('The total number of combinations =', len(all_combos))
    print('Time taken to achieve=', timer2-timer1)


#generates the dice combinations for words of 13 letters in length
def words_length13():
    timer1 = timer()
    gridLocations(4,4)
    all_combos = []
    multiCombos(4, 0)
    all_combos = all_combos + mixCombos
    pickle.dump(all_combos,open("legalCombinations4.p", "wb"))
    timer2 = timer()
    print('The total number of combinations =', len(all_combos))
    print('Time taken to achieve=', timer2-timer1)


#generates the dice combinations for words of 14 letters in length
def words_length14():
    timer1 = timer()
    gridLocations(4,4)
    all_combos = []
    multiCombos(3, 2)
    all_combos = all_combos + mixCombos
    pickle.dump(all_combos,open("legalCombinations5.p", "wb"))
    timer2 = timer()
    print('The total number of combinations =', len(all_combos))
    print('Time taken to achieve=', timer2-timer1)


#generates the dice combinations for words between 15 and 16 letters in length
def words_length15to16():
    timer1 = timer()
    gridLocations(4,4)
    all_combos = []
    all_combos2 = []
    combinations = [[4,1],[3,3]]
    for item in combinations:
        multiCombos(item[0], item[1])
        all_combos = all_combos + mixCombos
    pickle.dump(all_combos,open("legalCombinations6.p", "wb"))
    timer2 = timer()
    print('The total number of combinations =', len(all_combos))
    print('Time taken to achieve=', timer2-timer1)




