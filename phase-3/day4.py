#sudoko
'''b=[
    [0,5,0,0,0,0,0,0,7],
    [0,0,0,3,0,0,0,2,0],
    [0,0,0,1,0,0,0,0,0],
    [0,0,0,0,5,0,0,6,0],
    [0,0,5,0,0,9,0,0,0],
    [0,0,0,0,6,0,0,0,0],
    [0,0,8,0,0,4,0,0,0],
    [0,0,0,0,0,0,0,3,0],
    [0,7,0,0,0,0,1,0,0]
]
def find(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j]==0:
                return (i,j)
    else:
        return None
def isvalid(b,r,col,no):
    for i in range(len(b[0])):
        if b[r][i]==no:
            return False
    for i in range(len(b)):
        if b[i][col]==no:
            return False
    strow=3*(r//3)
    stcol=3*(col//3)
    for i in range(strow,strow+3):
        for j in range(stcol,stcol+3):
            if b[i][j]==no:
                return False
    return True
def play(b):
    empty=find(b)
    if empty==None:
        return False
    i,j=empty
    for no in range(1,10):
        if isvalid(b,i,j,no):
            b[i][j]=no
            if play(b):
                return True
            b[i][j]=0
    return False
if play(b):
    for i in b:
        print(i)
else:
    print("invalid")'''
#travelling salesman
'''m=[[0,10,30],
   [10,0,20],
   [30,20,0]
   #[40,25,30,0]
   ]
def findway(visited,pos):
    if len(visited)==len(m):
        return m[pos][0]
    md=999
    for city in range(len(m)):
        if city not in visited:
            visited=visited+[city]
            nd=m[pos][city]+findway(visited,city)
            md=min(md,nd)
    return md    
visited=[0]
print(findway(visited,0))'''
'''board=[
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]
def find(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return (i,j)
def isvalid(board,row,col,no):
    for i in range(len(board[0])):
        if board[row][i]==no:
            return False
    for j in range(len(board)):
        if board[j][col]==no:
            return False
    startrow=3*(row//3)
    startcol=3*(col//3)
    for i in range(startrow,startrow+3):
        for j in range(startcol,startcol+3):
            if board[i][j]==no:
                return False
    return True
def play(board):
    empty=find(board)
    if empty==None:
        return True
    i,j=empty
    for no in range(1,10):
        if isvalid(board,i,j,no):
            board[i][j]=no
            if play(board):
                return True
            board[i][j]=0
    return False
s=play(board)
if s==False:
    print("invalid")
else:
    for i in board:
        print(i)'''