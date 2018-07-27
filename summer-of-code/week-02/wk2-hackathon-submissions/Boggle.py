#txtFile = open("TextFile1.txt","r")
#dic = open("dictionary.txt","w")
#for line in txtFile:
#    if len(line)>3:
#        dic.write(line)
#txtFile.close()
#dic.close()

# find a word 


import random

def find_words_from_paths(board,paths):
    words = []
    
    for path in paths:
        word = ""
        for j in range(0,len(path),2):
            x=path[j]
            y=path[j+1]
            word = word+board[x][y]
        with open("Dictionary.txt") as dic:
            for w in dic:
                if (w[:-1]==word.lower()):
                    words.append (word)
    return words

def find_paths(board,position):    
    x = position[0]
    y = position[1]
    N = len(board)   
    #possible_words=[]
    search_list = []
    #syllabus=board[x][y]
    path=[x,y]
    first_tuple=([x,y],False,path)
    search_list.append(first_tuple)
    solution = []
    # search around the cell to find the connected cells and keep them in a list
        #The search will then continued with each cell in the list..one by one
    
    while search_list[len(search_list)-1][1]==False: #search till the last possible letter--False means this position hasn't been invistigated yet
        position = get_new_position4paths(search_list) 
        #syllabus = get_syllabus(position,search_list)
        path= get_path4paths(position,search_list)
        #syllabus1 = syllabus
        x = position[0]
        y = position[1]
        for i in [-1,0,1]:   # directions
            if x+i in range(0,N):
                for j in [-1,0,1]:
                    if y+j in range(0,N):
                        if (not(checked4paths([x+i,y+j],search_list,path))):
                            #if not(i==0 and j==0): #eleminate the current letter so the syllabus will not contain the same letter twice
                                 #syllabus1 = syllabus+board[x+i][y+j]
                            #possible_words=find_words_startsWith(syllabus1)
                            #if (possible_words!=[]):
                               # if possible_words[0]==syllabus1:
                                solution.append(path)
                                #print(path)
                                   
                                if not(i==0 and j==0):
                                    path1 = path + [x+i,y+j]
                                    search_list.append(([x+i,y+j],False,path1))

        search_list = set_as_checked4paths([x,y],search_list,True)
                                
    return solution

def get_path4paths(position,list):
    path=[]
    if(list!=[]):
        for l in list:
            if l[0]==position:
                if len(l)>2:
                    path = l[2]
    return path

def get_new_position4paths(list):
    position=[-1,-1]
    if list!=[]:
        for l in list:
           
            if l[1]==False:
                position[0]=l[0][0]
                position[1]=l[0][1]
                break
    return position

def checked4paths(position,list,path):
    check_flag=False
    path_flag=False
    if list!=[]:
        for l in list:
            if position==l[0]:
                check_flag=l[1]               
                for i in range(0,len(path),2):
                    if path[i]==position[0] and path[i+1]==position[1]:
                        path_flag=True
                        break
    return (check_flag and path_flag)

def set_as_checked4paths(position,list,flag):
    if list!=[]:
        for i in range(0,len(list)):
            if position==list[i][0]:
                list[i] = list[i][:1]+(flag,)
                
    return list



def find_solution(board,position):    
    x = position[0]
    y = position[1]
    N = len(board)   
    possible_words=[]
    search_list = []
    syllabus=board[x][y]
    path=[x,y]
    first_tuple=([x,y],syllabus,False,path)
    search_list.append(first_tuple)
    solution = []
    # search around the cell to find the connected cells and keep them in a list
        #The search will then continued with each cell in the list..one by one
    
    while search_list[len(search_list)-1][2]==False: #search till the last possible letter--False means this position hasn't been invistigated yet
        position = get_new_position(search_list) 
        syllabus = get_syllabus(position,search_list)
        path= get_path(position,search_list)
        syllabus1 = syllabus
        x = position[0]
        y = position[1]
        for i in [-1,0,1]:   # directions
            if x+i in range(0,N):
                for j in [-1,0,1]:
                    if y+j in range(0,N):
                        if (not(checked([x+i,y+j],search_list,path))):
                            if not(i==0 and j==0): #eleminate the current letter so the syllabus will not contain the same letter twice
                                 syllabus1 = syllabus+board[x+i][y+j]
                            possible_words=find_words_startsWith(syllabus1)
                            if (possible_words!=[]):
                                if possible_words[0]==syllabus1:
                                   solution.append(syllabus1)
                                   
                                if not(i==0 and j==0):
                                    path1 = path + [x+i,y+j]
                                    search_list.append(([x+i,y+j],syllabus1,False,path1))

        search_list = set_as_checked([x,y],search_list,True)
                                
    return solution

def find_words_startsWith(syllabus):
    words_list=[]
    with open("Dictionary.txt","r") as dic:
        for word in dic:
            #could be optimized based on the letter position
            if word[0]>syllabus[0]:
                break
            else:
                if word[:len(syllabus)]==syllabus:
                    words_list.append(word[:-1])
    return words_list

# Return the position (x,y) from a list of tuples where the flag is False: False means the letter haven't been invistigated yet
def get_new_position(list):
    position=[-1,-1]
    if list!=[]:
        for l in list:
           
            if l[2]==False:
                position[0]=l[0][0]
                position[1]=l[0][1]
                break
    return position

def get_syllabus(position,list):
    syllabus=""
    if list!=[]:
        for l in list:
            if l[0]==position:
                syllabus=l[1]
    return syllabus

def get_path(position,list):
    path=[]
    if(list!=[]):
        for l in list:
            if l[0]==position:
                if len(l)>3:
                    path = l[3]
    return path

def checked(position,list,path):
    check_flag=False
    path_flag=False
    if list!=[]:
        for l in list:
            if position==l[0]: 
                check_flag=l[2]                
                for i in range(0,len(path),2):
                    if path[i]==position[0] and path[i+1]==position[1]:
                        path_flag=True
                        break
    return (check_flag and path_flag)

def exist(position,list):
    flag = False
    if list!=[]:
        for l in list:
            if l[0]==position:
                flag=True
    return flag

def set_as_checked(position,list,flag):
    if list!=[]:
        for i in range(0,len(list)):
            if position==list[i][0]:
                list[i] = list[i][:2]+(flag,)
                
    return list

def unique(list):
    list = sorted(list)
    ulist = []
    for i in list:
        found = False
        for j in ulist:
            if i==j:
                found = True
        if not found:
            ulist.append(i)
    return ulist
    
def calculate_score(list):
    score = 0
    for w in list:
        score = score + len(w)-2
    return score

import random
#generate board

dice = [['A','A','E','E','G','N'],
        ['E','L','R','T','T','Y'],
        ['A','O','O','T','T','W'],
        ['A','B','B','J','O','O'],
        ['E','H','R','T','V','W'],
        ['C','I','M','O','T','U'],
        ['D','I','S','T','T','Y'],
        ['E','I','O','S','S','T'],
        ['D','E','L','R','V','Y'],
        ['A','C','H','O','P','S'],
        ['H','I','M','N','Q','U'],
        ['H','I','M','N','Q','U'],
        ['E','E','I','N','S','U'],
        ['E','E','G','H','N','W'],
        ['A','F','F','K','P','S'],
        ['H','L','N','N','R','Z'],
        ['D','E','I','L','R','X']]
N=4

index = 0
N = 4
board=[[0 for i in range(0,N)] for i in range(0,N)]
for i in range(0,N):
    for j in range(0,N):
        index=index+1
        r = random.randint(0,N)
        board[i][j]=(dice[index][r]).lower()


for i in board:
    print(i)
paths = []
solution = []
N = 4
#print ("score=",score)
for i in range(0,N):
    for j in range(0,N):
        solution = solution + find_solution(board,[i,j])
solution = unique(solution)
# print(solution)
score = calculate_score(solution)


print("\n\n")
results={"score":score,"words":solution}
print(results)

# calculate the maximum number of words
for i in range(0,N):
    for j in range(0,N):
        paths = paths + find_paths(board,[i,j])
#
#
paths = unique(paths)
print("The maximum number of words is: " ,len(paths))




