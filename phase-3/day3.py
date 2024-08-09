#snake and ladder
#n queens

'''def issafe(b,i,j,n):
    orgi=i
    orgj=j
    for col in range(n):
        if b[i][col]=="Q":
            return False
    for r in range(n):
        if b[r][j]=="Q":
            return False
    while i>=0 and i<n and j>=0 and j<n :
        if b[i][j]=="Q":
            return False
        i-=1
        j-=1
    i=orgi
    j=orgj 
    while i>=0 and i<n and j>=0 and j<n :#upper diagonal
        if b[i][j]=="Q":
            return False
        i-=1
        j+=1 
    return True
def play(b,r,col,n):
    if r==n:
        for i in b:
            print(i)
        exit()
    for i in range(col):
        if issafe(b,r,i,n):
            b[r][i]="Q"
            play(b,r+1,col,n)
            b[r][i]=0
n=int(input("Queens?"))
b=[[0]*n for i in range(n)]
play(b,0,n,n)'''
#knapsack
'''val=[200,150,50]
wt=[10,20,30]
cap=50
def knap(val,wt,cap,n):
    if n==0 or cap==0:
        return 0
    if wt[n-1]>cap :
        knap(val,wt,cap,n-1)
    else:
        return max(val[n-1]+knap(val,wt,cap-wt[n-1],n-1),knap(val,wt,cap,n-1))
n=len(val)
print(knap(val,wt,cap,n))
'''
#snake and ladder game with 2 players

import random
snake={24:5,38:12,47:23,70:36,80:55} # snake
ladder={4:20,15:35,28:50,39:58,53:95} #ladder
def movedice(playerpos,dice):
    newpos=playerpos+dice
    if newpos in snake:  #snake
        newpos=snake[newpos]
        print("you are bitten by a snake")
        return newpos
    elif newpos in ladder:
        if newpos in ladder:  #ladder
            newpos=ladder[newpos]
            print("you found a ladder")
    if newpos>100:
        print("invalid dice number, greater than zero try again")
        return playerpos            
    return newpos
    
def printboard(p1,p2):
    pos1=p1%10
    pos2=p2%10
    
    for i in range(9,-1,-1):
        for j in range(1,11):
            c=0
            newno=i*10+j
            # newno=(j-10)*10+i
            if p1==newno:
                print("*p1",end=" ")
                c=1
            if p2==newno:
                print("*p2",end=" ")
                c=1
            if c==0:
                if newno in snake :
                    print(" S ",end=" ")
                elif newno in ladder:
                    print(" L ",end=" ")
                else:
                    print(" _ ",end=" ")
        print()

def diceroll():
    return random.randint(1,6)

print('-'*50)
print("welcome to snake and ladder game\n**  Player1 and Player2  **")
print('-'*50)
playerpositions=[0,0]
leadingpos=0
p=1
while leadingpos!=100:
    
    print(f"player{1} and player{2} positions are {playerpositions[0],playerpositions[1]}.\nNow player{p} turn")
    input("press enter to roll dice")
    dice=diceroll()
    print("your lucky number is",dice)
    move=movedice(playerpositions[p-1],dice)
    print("your new position is ", move)
    playerpositions[p-1]=move
    print()
    printboard(playerpositions[0],playerpositions[1])
    print('*'*55)
    leadingpos=max(playerpositions)
    if p==1:
        p=p+1
    else:
        p-=1
winner=playerpositions.index(100)
print("\n\n")
print(f"congratulations to player{winner+1}, you won")
print("\n\n")

'''
#word search
b=[['m','e','y','c','l'],
   ['a','v','t','y','f'],
   ['n','a','e','r','w'],
   ['e','s','w','h','v'],
   ['r','m','i','n','i']
   ]
w="manaswini"
n=len(w)
def find(r,c,i,n,path):
    if i==n:
        print("Valid")
        print(path)
        exit()
    if i==0 or i>=n or j==0 or j>=n:
        return False 
    if [r,c] not in path:
        path.append([r,c])
        if b[r][c]==w[i]:
            if find(r+1,c,i+1,n,path):
                return True
            if find(r-1,c,i+1,n,path):
                return True
            if find(r,c+1,i+1,n,path):
                return True
            if find(r,c-1,i+1,n,path):
                return True
        path.remove([r,c])
    return False
path=[]
for i in range(len(b)):
    for j in range(len(b[0])):
        if find(i,j,0,n,path):
            break'''

            
