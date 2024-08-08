#pangrams
#approach1
'''s=input()
s1=set(s)
if len(s1)>=26:
    print("pandrome")
else:
    print("not pandrome")'''
#approach 2
'''s=input()
d={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
d1{}
for i in s:
    for i in d:
        for i not in d1:
            d[i]=1
        else:
            d[i]+=1'''
'''t=int(input())
for i in range(t):
    s=input()
    l=list[s]
    d={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    d1={}
    for i in l:
        for i in d:
            if i not in d1:

                d1[i]=1
            else:
                d1[i]+=1
    for i in d1:
        if d[i]>=2:
            print(i)
        else:
            print(".")'''
#dict and map
'''n=int(input())
d={}
for i in range(d):
    name,num=map(input().split())
    d[name]=num'''
'''n=int(input())
d={}
for i in range(n):
    s=input()
    if s in d:
        d[s]=d[s]+1
    else:
        d[s]=1
m=max(d)
l=[]
for i in d:
    if d[i]==m :
        l.append(i)
print(max(l),m)'''
#subjects
'''t=int(input())
for i in range(t):
    n,r=map(int,input().split())
    d={}
    for i in range(r):
        s,c=map(int,input().split())
        l=[]
        if c in d:
            d[c].append(s)
        else:
            d[c]=[s]
    print(d)
    for i in d:
        if len(d[i])>n and len(set(d[i])==len(d[i])):
            print(f"scenario #(i+1) : Impossible")
        else:
            print(f"scenario #(i+1) : possible")'''
#graph
n=int(input())
d={}
for i in range(n):
    a,b=input().split()
    l=[]
    if a in d:
        d[a].append(b)
    else:
        d[a]=[b]
print(d)
q=input()
if q in d:
    print(d[q])
else:
    print("none")











    




    
    
        
        

    


        



