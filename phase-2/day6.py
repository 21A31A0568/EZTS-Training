#linear
'''l=list(map(int,input().split()))
k=int(input())
for i in l:
    if i==k:
        print("successful")
        exit()
else:
    print("unsuccessful")'''
#binary
'''ls=list(map(int,input().split()))
k=int(input())
l=0
h=len(ls)-1
while l<h:
    m=(l+h)//2
    if ls[m]==k:
        print("yes")
        exit()
    elif ls[m]>k:
        l=m-1
    elif ls[m]<k:
        h=m+1'''
#bubble sort-for every iteration largest number will come to last place
'''l=list(map(int,input().split()))
for i in range(0,len(l)-1):
    for j in range(0,len(l)-1-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)'''
#selection sort-for every iteration small number will come to small place
'''l=list(map(int,input().split()))
for i in range(0,len(l)-1):
    m=i
    for j in range(i+1,len(l)):
        if l[j]<l[m]:
            m=j
    l[i],l[m]=l[m],l[i]
print(l)'''
#insertion sort- 
l=list(map(int,input().split()))
for i in range(1,len(l)):
    k=l[i]
    j=i-1
    while j>=0 and l[j]>k:
        l[j+1]=l[j]
        j-=1
    l[j+1]=k
print(l)

    


    
    
