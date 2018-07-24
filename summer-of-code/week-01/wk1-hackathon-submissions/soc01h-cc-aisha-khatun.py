##input size of civilization
import random
n=(int)(input("size of civilization? : "))
ara=[ [0]*n for i in range(n)]
# print(ara)
for i in range(0,n):
    for j in range (0,n):
        ara[i][j]=random.randrange(0,2)
## 1 means land, 0 means sea
for i in range(0,n):
    for j in range (0,n):
        print(ara[i][j],end=" ")
    print("")

dx=[0,0,1,-1]
dy=[1,-1,0,0]
flag=[ [0]*n for i in range(n)]
cnt=0

def dfs(x,y):
    flag[x][y]=1
    global cnt
    cnt=cnt+1
    for i in range (0,4):
        ax=x+dx[i]
        ay=y+dy[i]
        if ax>=0 and ay>=0 and ax<n and ay<n and flag[ax][ay]==0 and ara[ax][ay]==1:
            dfs(ax,ay)
    return

cont_siz=[]
for i in range(0,n):
    for j in range (0,n):
        if flag[i][j]==0 and ara[i][j]==1:
            cnt=0
            dfs(i,j)
            cont_siz.append(cnt)

print(cont_siz)