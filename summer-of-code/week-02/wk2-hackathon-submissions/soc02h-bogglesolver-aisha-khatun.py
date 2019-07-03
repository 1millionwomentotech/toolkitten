filename="dictionary.txt"
file = open(filename,'r')

print("---please wait while the dictionary loads---")
dic=dict()
for line in file:
    line=line.strip()
    dic[line]=True

frequency={
    "a":6,"b":2,"c":2,"d":3,"e":11,"f":2,"g":2,"h":5,"i":6,
    "j":1,"k":1,"l":4,"m":2,"n":6,"o":7,"p":2,"q":1,"r":5,"s":6,
    "t":9,"u":3,"v":2,"w":3,"x":1,"y":3,"z":1
}

n=(int)(input("board size? (min 3): "))
print("---creating board---")
if n < 3:
    n=3
board=[ [0]*n for i in range(n) ]

import random
for i in range(n):
    for j in range(n):
        while(1):
            x=chr(random.randint(65,65+25))
            if(frequency[x.lower()]>0):
                board[i][j]=x
                frequency[x.lower()]-=1
                break

for i in range(n):
    for j in range(n):
        print(board[i][j],end=" ")
    print("\n")

dx=[0,0,1,-1]
dy=[-1,1,0,0]

words=set()
result={
    "score":0,
    "words":[]
}

flag=[ [0]*n for i in range(n) ]

def dfs(i,j,str):
    # print(i," ",j)
    if (str in dic) and len(str)>2:
        words.add(str)
        # print("aise ",i," ",j)
        # print(str)

    if i<0 or j<0 or i>=n or j>=n or flag[i][j]==True:
        return

    flag[i][j]=True

    for k in range(4):
        x=i+dx[k]
        y=j+dy[k]
        dfs(x,y,str+board[i][j])

    flag[i][j]=False
    return

# import sys

# orig_stdout = sys.stdout
# f = open('out.txt', 'w')
# sys.stdout = f

for i in range(n):
    for j in range(n):
        flag=[ [0]*n for i in range(n) ]
        dfs(i,j,"")

# sys.stdout = orig_stdout
# f.close()

for str in words:
    result["score"]+=len(str)-2
result["words"]=words
print(result)