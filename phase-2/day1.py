
#stacks
'''class stacks:
    def __init__(self):
        self.l=[]
        self.s=5
    def push(self,n):
        if self.l!=self.s :
            self.l.append(n)
            print(self.l)
        else:
            print ("Notpossible")
    def pop(self):
        if len(self.l)==0:
            print("error")
        else:
            self.l.pop()
            print(self.l)
    def peek(self):
        if len(self.l)==0:
            print("error")
        else:
            print(self.l[-1])
obj=stacks()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.pop()
obj.peek()        
'''
#s=54367+-*=
'''s=input()
l1=[]
for i in range(len(s)):
    if s[i].isdigit():
        l1.append(int(s[i]))
    else:
        a=l1.pop()
        b=l1.pop()
        if s[i]=='+' :
            l1.append(a+b)
        elif s[i]=='-':
            l1.append(a-b)
        elif s[i]=='*':
            l1.append(a*b)
print(l1[0])'''
#n=3
s=[1,2,3,4,5,6,7,8,9,10,11,12]
n=3
flag=0
while len(s)>1:
    if flag==0:
        for i in range(n):
            if len(s)>1:
                s.pop(0)
            else:
                break
        flag=1
    else:
        for i in range(n):
            if len(s)>1:
                s.pop(-1)
            else:
                break
        flag=0
print(s[0])

