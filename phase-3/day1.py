#fibnacci using tabulation
'''n=10
m=[0]*(n+1)
m[1]=1
for i in range(2,n+1):
    m[i]=m[i-1]+m[i-2]
print(m)'''
#coin denomination
coin=[1,2,5]
amt=5
m=[0]*(amt+1)
for i in coin:
    for j in range(i,amt+1):
        m[j]=m[j-i]+1
print(m[amt]) 