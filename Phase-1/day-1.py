# print many hello worlds
'''i=0
for i in range(1000):
    print("Hello World") 
'''
#small large or equal
'''a,b=map(int,input().split())
if (a<b):
    print("a lessthan b")
elif (a>b):
    print("b greater yhan a")
else:
    print("a equals to b")'''
#triangle validator 
'''a,b,c=map(int,input().split())
if (a+b>c and b+c>a and a+c>b):
    print("Yes")
else :
    print("No")
'''
#apples in basket
'''n=int(input())
k=int(input())
while (k>n):
    k=k-n
print(k)'''
#number inverse
'''n=int(input())
r=0
e=0
if(n<0):
    e=n
    n=-n
while(n):
    k=n%10
    r=r*10+k
    n=n//10
if e<0:
    print(-r)
else:
    print(r)
'''
'''#watermelon
w=int(input())
if (w>2 and w%2==0):
    print("Yes")
else:
    print("No")
'''
#fever
'''for i in range(int(input())):
    t=int(input())
    print("Yes" if t>98 else "No")
'''
#discount
'''for i in range(int(input())):
    print(100-int(input()))
'''
#tv discount
'''for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    if ((a-c) > (b-d)):
        print("Second")
    elif((a-c) == (b-d)):
        print("Any") 
    else:
        print("First")'''
#candy
'''for i in range(int(input())):
    n,x=map(int,input().split())
    if (x>=n) :
        print(0)
    else:
        e=n-x
        if (e%4==0):
            print(e//4)
        else:
            print((e//4)+1)'''
#pizza
for i in range(int(input())):
    n,x=map(int,input().split())
    t=n*x
    p=0
    while(t>=4):
        p=p+1
        t=t-4
    print(p if t==0 else p+1)






