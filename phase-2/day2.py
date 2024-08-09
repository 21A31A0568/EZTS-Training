#manual
class node:
    def __init__ (self, data):
        self.data=data
        self.next=None
'''a=node(1)
b=node(2)
c=node(3)
a.next=b
b.next=c
print(a.data,a.next.data,a.next.next.data)
'''
#insertion
class linkedlist:
    def __init__(self):
        self.head=None
        self.count=0
    def insertatbeg(self,value):
        newnode=node(value)
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def insertatend(self,value):
        newnode=node(value)
        if self.head==None:
            self.head=newnode
        else:
            cur=self.head
            while cur.next!=None :
                cur=cur.next
            cur.next=newnode
    def insertatmid(self,value):
        newnode=node(value)
        if self.head==None:
            self.head=newnode
        if self.count==1:
            self.head.next=newnode
        else:
            f=self.head
            s=self.head
            while f.next!=None and f.next.next!=None:
                f=f.next.next
                s=s.next
            newnode.next=s.next
            s.next=newnode
    '''def delatmid(self):
    def delatbeg(self):
        if self.head==None:
            print("list is empty")
            return 0
        else:
            self.head=self.head.next
    def delatend(self):
        if self.head==None:
            print("list is empty")
            return 0
        else:
            cur=self.head
            while cur.next.next:
                cur=cur.next
            cur.next=None'''
    def reverse(self):
        p=None
        n=None
        c=self.head
        while c!=None:
            n=c.next
            c.next=p
            p=c
            c=n
        self.head=p
    def print(self):
        cur=self.head
        while(cur!=None):
            print(cur.data,end="->")
            cur=cur.next
        print("null")
    def countlist(self):
        cur=self.head
        while cur!=None:
            self.count+=1
            cur=cur.next
        return self.count
l=linkedlist()
l.insertatbeg(1)
l.insertatbeg(2)
l.insertatbeg(3)
l.insertatbeg(4)
l.insertatend(5)
#l.delatbeg()
#l.delatend()
#l.insertatmid(6)
print(l.countlist())
l.reverse()
l.print()


