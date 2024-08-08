#Problem Statement 1
n = int(input())
l = list(map(int,input().split()))
for i in range(n):
    if l[i] in l[i+1:n]:
        print(l[i])
        break

#Problem Statement 2 
n = int(input())
l = list(map(int,input().split()))
for i in range(n):
     if l[i] not in l[i+1:n] and l[i] not in l[:i]:
        print(l[i])

#Problem Statement 3
n = int(input())
l = []
l1 =[]
for i in range(1,n+1):
   if n%i==0 and i%2==0:
        l.append(i)
   elif n%i==0 and i%2==1:
        l1.append(i)
if l and l1:
    print("1")
else:
    print("0")

#Problem Statement 4
a = int(input())
for i in range(a):
    n,x  = map(int,input().split())
    l = list(map(int,input().split()))
    c = list(map(int,input().split()))
    p = 0
    for j in range(n):
        if l[j]>=x:
            p +=c[j]
    print(p)

#Problem Statement 5
a = int(input())
l = list(map(int,input().split()))
c = list(map(int,input().split()))
e = 0
for i in range(a):
    if l[i]*2>=c[i] and l[i]<=c[i]*2:
        e+=1
print(e) 

#Problem Statement 6
a = int(input())
for i in range(2,a):
    if a%i==0:
        print("Not Prime")
        break
else:
    print("Prime")

#Problem Statement 7 
a = int(input())
for i in range(2,a+1,2):
   s = 0
   for j in range(1,i):
        if i%j ==0:
            s+=j
   if s==i:
       print(i,end=" ")
            

