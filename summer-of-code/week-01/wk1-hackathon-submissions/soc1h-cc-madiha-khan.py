world=[[0,0,1,1,1,0,0,0,1,1,0],[1,0,0,0,1,1,1,1,0,0,0],[0,0,1,1,1,0,0,0,0,1,1],
[0,1,0,1,1,1,0,0,0,0,1],[1,0,0,1,0,0,1,1,1,0,0],[1,1,1,0,0,1,0,0,1,1,1],[1,0,0,0,1,1,1,0,0,0,0],
[0,0,1,1,0,0,0,1,1,0,1],[0,1,1,0,0,1,1,1,0,0,1],[0,0,1,0,1,0,0,1,1,0,0],[1,0,0,1,1,0,0,0,1,1,0]]
check=[[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0]]

cent_arr=[5,5]
concounter=0


def checkc(num1,num2,count):
	global cc
	cc = count
	if world[num1][num2]==1 and check[num1][num2]==0 and num1 >=0 and num2 <=11:
		cc=cc+1
		check[num1][num2]=1
		cc=sequence(num1,num2,cc)
		del cent_arr[0]
		del cent_arr[0]
		return cc
	elif world[num1][num2]==1 and check[num1][num2]==1 and num1>=0 and num2 <=11:
		cc=sequence(num1,num2,cc)
		del cent_arr[0]
		del cent_arr[0]
		return cc
	elif world[num1][num2]==0 and check[num1][num2]==0 and num1>=0 and num2 <=11:
		check[num1][num2]=1
		del cent_arr[0]
		del cent_arr[0]
		return cc
	else:
		del cent_arr[0]
		del cent_arr[0]
		return cc
		#check(cent_arr)

	#elif len(cent_arr)<=1:
	#	return

def sequence(num1,num2,count):
	global cc
	cc=count					
	i=1
	if  num1>0 and num2 <11 and num2>0 and world[num1-i][num2-i]==1 and check[num1-i][num2-i]==0:	#upper left diagonal
		cc=cc+1
		check[num1-i][num2-i]=1
		cent_arr.extend([num1-i,num2-i])
	elif num1>0  and num2>0 and world[num1-i][num2-i]==0 and check[num1-i][num2-i]==0:
		check[num1-i][num2-i]=1
	else:
		pass

	if num1>0 and num2<=11 and world[num1-i][num2]==1 and check[num1-i][num2]==0:		#upper diagonal
		cc=cc+1
		check[num1-i][num2]=1
		cent_arr.extend([num1-i,num2])
	elif num1>0 and  world[num1-i][num2]==0 and check[num1-i][num2-i]==0:
		check[num1-i][num2]=1
	else:
		pass
	if num1>0 and num2<10 and world[num1-i][num2+i]==1 and check [num1-i][num2+i]==0: 	#upper right diagonal
		cc=cc+1
		check[num1-i][num2+i]=1
		cent_arr.extend([num1-i,num2+i])
	elif num1>0 and num2<10 and world[num1-i][num2+i]==0 and check[num1-i][num2+i]==0:
		check[num1-i][num2+i]=1
	else:
		pass

	if num1>=0 and num2<10 and world[num1][num2+i]==1 and check[num1][num2+i]==0:		# right diagonal
		cc=cc+1
		check[num1][num2+i]=1
		cent_arr.extend([num1,num2+i])
	elif num1 >=0 and num2<10 and world[num1][num2+i]==0 and check[num1][num2+i]==0:
		check[num1][num2+i]=1
	else:
		pass
	if num1<10 and num2>=0 and num2<10 and world[num1+i][num2+i]==1 and check[num1+i][num2+i]==0:		#lower right diagonal
		cc=cc+1
		check[num1+i][num2+i]=1
		cent_arr.extend([num1+i,num2+i])
	elif num1<10 and num2<10 and num2>=0 and world[num1+i][num2+i]==0 and check[num1+i][num2+i]==0:
		check[num1+i][num2+i]=1
	else:
		pass
	if  num1<10 and num2<11 and world[num1+i][num2]==1 and check[num1+i][num2]==0:		#lower diagonal		
		cc=cc+1
		check[num1+i][num2]=1
		cent_arr.extend([num1+i,num2])
	elif num1<10 and num2<11 and world[num1+i][num2]==0 and check[num1+i][num2]==0:
		check[num1+i][num2]=1
	else:
		pass
	if num1<10 and num2<11 and num2>0 and world[num1+i][num2-i]==1 and check[num1+i][num2-i]==0:		#lower left diagonal
		cc=cc+1
		check[num1+i][num2-i]=1
		cent_arr.extend([num1+i,num2-i])
	elif num1<10 and num2>0:
		check[num1+i][num2-i]=1
	else:
		pass
	if num1<10 and num2>0 and world[num1][num2-1]==1 and check[num1][num2-1]==0:		#left diagonal
		cc=cc+1
		check[num1][num2-i]=1
		cent_arr.extend([num1,num2-i])
	else:
		check[num1][num2-i]=1
	return cc
j=len(cent_arr)
while j>=1:
	#for i in range(len(cent_arr)):
	a=cent_arr[0]
	b=cent_arr[1]
	concounter=checkc(a,b,concounter)
	j=len(cent_arr)/2
	
	if len(cent_arr)<1:
		break			
print ("world\n")
print("We are standing at 5,5")
for i in range(len(world)):
	print('\n')
	for j in range(len(world[i])):
		print(world[i][j], end=' ')
print ("\n\ntotal connected lands or continent size is: " + str(concounter))

		






	




		




		

	

