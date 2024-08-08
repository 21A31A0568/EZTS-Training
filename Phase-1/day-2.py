#pass by reference
'''def myFun(x):
    x[0]=40
lst=[10,20,30]
myFun(lst)
print(lst)'''
#sugarcane
'''def sugarcane(x):
    t=x*50
    p=int(t*(70/100))
    return (t-p)
def rec(t):
    if(t>0):
        n=int(input())
        print(sugarcane(n))
    else:
        return
    rec(t-1)
t=int(input())
rec(t)'''
#movie
'''def movie(a,b):
    print(a-(b//2))
x,y=map(int,input().split())
movie(x,y)'''
#lucky4
'''t=int(input())
def cou(n):
    c=0
    if (n>0 and ((n%10)==110)):                              
        c=c+1
        n=cou(n//10)
    else:
        return 0
    return c
def count(n):
    c=0                                                   
    while(n):                                             
        if ((n%10)==4):                                  
            c=c+1                                         
        n=n//10
    return(c)
def rev(t):
    if t>0:
        n=int(input())
        print(cou(n))
    else:
        return
    t=rev(t-1)
rev(t) '''   
#compute n!
'''n=int(input())
def fact(n):
    if n<=1:
        return 1
    else:
        n=n*fact(n-1)
    return n
print(fact(n))
for i in range(1,n+1):
     r=r*i
'''
#append 3
'''n=int(input())
def rev(n):
    r=0
    while(n):
        k=n%10
        r=(r*10)+k
        n=n//10
    return r
def app(n):
    n=(n*10)+3
    return rev(n)
a=app(n)
print(app(a))'''
n=int(input())
r=0
for i in range(2):
     n=(n*10)+3
     while(n):
        k=n%10
        r=(r*10)+k
        n=n//10
print(r)



    
    



  
