#tower of hanoi
'''def tower(n,s,e,d):
    if n==1:
        print("move",n,"from",s,"to",d)
        return
    tower(n-1,s,d,e)
    print("move",n,"from",s,"to",d)
    tower(n-1,e,s,d)
n=3
tower(n,"source","extra","destiny")'''
#tic tac toe
def printb(b):
    print("*"*20)
    for row in b:
        print("      |".join(row))
        print("-"*18)
    print("*"*20)
def full(b):
    for row in b:
        for col in row:
            if col=="":
                return False
    return True
def check(b,cur):
    for i in range(3):
        if b[i][0]==cur and b[i][1]==cur and b[i][2]==cur:
            return True
    for col in range(3):
        if b[0][col]==cur and b[1][col]==cur and b[2][col]==cur:
            return True
    if b[0][0]==cur and b[1][1]==cur and b[2][2]==cur:
            return True
    if b[0][2]==cur and b[1][1]==cur and b[2][0]==cur:
            return True
    return False
b=[[""]*3 for i in range(3)]
print("welcome")
printb(b)
print("player x or o")
cur='x'
while True:
    print("current player is ",cur)
    print("enter dimension")
    x,y=map(int,input().split())
    if 0<=x<3 and 0<=y<3:
        b[x][y]=cur
        printb(b)
        if check(b,cur):
            print("player",cur,"winner")
            break
        if full(b):
            print("draw")
            break
        if cur=="x":
            cur="o"
        else:
            cur="x"        
    else:
        print("invalid dimensions")
    


