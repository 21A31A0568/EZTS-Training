#oddeven
'''s=input()
print(s[1::2]+s[0::2])'''
#occurance of a character
'''s=input()
s=s.lower()
ch=input()
c=0
for i in s:
    if ch == i:
        c=c+1
print(c)'''
#occurance of a character at even
'''s=input()
s=s.lower()
ch=input()
c=0
for i in range(len(s)):
    if ch == s[i] and i%2==0:
        c=c+1
print(c)'''
#vowels in string 1 ,2
'''s=input()
s=s.lower()
v="aeiou"
c=0
for i in s:
    if i in v:#if i not in v: 
        c=c+1
if len(s)==c:#c==0
    print("Yes")
else:
    print("No")'''
#3
'''
s=input()
v="aeiouAEIOU"
for i in s:
    if i not in v:
        print("No")
        break
else:
    print("Yes")'''
#digit 1
'''
s=input()
d="0123456789"
for i in s:
    if i not in d:
        print("No")
        break
else:
    print("Yes")'''
#2 3
'''s=input()
d="0123456789"
c=0
for i in s:
    if i in d:#if i not in d: 
        c=c+1
if len(s)==c:#c==0
    print("Yes")
else:
    print("No")'''
#4
'''
s=input()
d=s.isdigit()
if d==True:
    print("Yes")
else:
    print("no")'''
#count vowel and consonants 1
'''s=input()
v="aeiouAEIOU"
d="0123456789"
vc=0
cc=0
dc=0
for i in s:
    if i in v:
        vc=vc+1
    elif i in d:
        dc=dc+1
    else:
        cc=cc+1
print(vc,cc)'''
#2

#compress string
'''s=input()
v=""
c=1
for i in range(len(s)):
    if i!=len(s) and'''
#words vowels consonants 1
'''t=int(input())
for i in range(t):
    s=list(input().split())
    vc=0
    cc=0
    wc=len(S) 
    for j in s:
         for k in j:
              if k.isalpha():
                   if k in n:
                        vc=vc+1
                    else:
                        cc=cc+1
    print(wc,vc,cc)'''
#2
'''t=int(input())
for i in range(t):
    s=list(input().split())
    vc=0
    cc=0
    wc=len(S) 
    for j in s:
        if j.isalpha():
            if j in n:
                vc=vc+1
            else:
                cc=cc+1
    print(wc,vc,cc)'''
'''t=int(input())
for i in range(t):
    s=input()
    c=0
    for j in (len(s)-1):
        if j==" " :
            c=c+1
    print(c) '''
#n-guess the problem
'''t=int(input())
for i in range(t):
    a,b=input().split()
    c=""
    for j in b:
        if j not in a:
            c=c+j
    print(c)'''
#+10 sum
'''for i in range(int(input())):
    a,b=input().split()
    b=int(b)
    c=""
    for i in a:
        ac=ord(i)+b
        if ac>122:
            ac= 96 + (ac-122)
            c=c+chr(ac)
        else:
            c=c+chr(ac)
    print(c)'''
#oops
class classa:
    def factorial(n):
        if n<=1:
            print(1)
        else:
            n=n*fact(n-1)
        print(fact(n))














               
