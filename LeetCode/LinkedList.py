class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,newnode):
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode

    def see(self):
        temp=self.head
        count=0
        while temp:
            print(temp.data)
            count+=1
            temp=temp.next
        print(count)

    def addstart(self,newnode):
        newnode.next = self.head
        self.head = newnode
        



n1=Node(20)
n2=Node(30)
n3=Node(40)

list=LinkedList()
list.append(n1)
list.append(n2)
list.append(n3)
list.see()

        