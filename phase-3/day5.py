#recursion limit
'''import sys
sys.setrecursionlimit(10000)
def fun(n):
    print(n)
    fun(n+1)
fun(1)'''
#compare two strings without using comparision operator
'''s1='manu'
s2='mana'''
#swap
'''a=5
b=6
a=a+b
b=a-b
a=a-b
print(a,b)'''
#knight problem
n=int(input("Enter a number greater than 7:"))
board=[[-1]*n for i in range(n)]
kmoves=[(-1,2),(1,2),(-2,1),(-2,-1),(1,-2),(-1,-2),(2,-1),(2,1)]
def issafe(r,c,b,n,moves):
    return 0<=r<n and 0<=c<n and b[r][c]==-1
def knight(b,row,col,n,moves):
    if moves==n*n:
        for i in b:
            print(i)
        return True
    for c in kmoves:
        newrow=row+c[0]
        newcol=col+c[1]
        if issafe(newrow,newcol,b,n,moves):
            b[newrow][newcol]=moves
            if knight(b,newrow,newcol,n,moves+1):
                return True
            b[newrow][newcol]=-1
    return False
board[0][0]=0
knight(board,0,0,n,1)
#graph coloring
'''graph=[[0,1,1,0],
       [1,0,0,1],
       [1,0,0,1],
       [0,1,1,0]]
def issafe(ver,col,t):
    for i in range(t):
        if graph[ver][i]==1 and color[i]==col:
            return False
        return True
def play(color,n,ver,t):
    if ver==t:
        print(color)
        return True
    for col in range(1,n+1):
        if issafe(ver,col,t):
            color[ver]=col
            if play(color,n,ver+1,t):
                return True
            color[ver]=0
    return False
n=3
color=[0]*len(graph)

play(color,n,0,len(graph))'''