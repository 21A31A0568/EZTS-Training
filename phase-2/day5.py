'''class Graph:
    def __init__(self):
        self.d={}
    def add(self,u,v):
        if u not in self.d:
            self.d[u]=[]
            self.d[u].append(v)
        else:
           self.d[u].append(v)
    def bfs(self,root):
        queue=[root]
        visited=[root]
        while queue:
            temp=queue.pop(0)
            for i in self.d[temp]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)
        return visited
g=Graph()
g.add(1,2)
g.add(1,3)
g.add(2,1)
g.add(2,4)
g.add(2,5)
g.add(3,1)
g.add(3,6)
g.add(3,7)
g.add(4,2)
g.add(5,2)
g.add(6,3)
g.add(7,3)
print(g.d)
print(g.bfs(1))
'''
l = [[1,1,0,1],
     [0,0,0,1],
     [1,0,0,1],
     [1,1,0,1]]
c = 0
def back(i,j):
    if j+1<4:
        if l[i][j+1] == 1 :
            l[i][j+1] = 0
            back(i,j+1)
    if i+1<4:
        if l[i+1][j] == 1:
                l[i+1][j] = 0
                back(i+1,j)
    return
        
for i in range(4):
    for j in range(4):
        if l[i][j] == 1 :
            #print(i,j)
            c += 1
            back(i,j)
print(c)
