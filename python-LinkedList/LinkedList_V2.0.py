# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 20:16:08 2021

@author: LENOVO
"""

#LINKED LIST V2.0

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None 
    
    def ListPrint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def AddHead(self,newdata):
        newnode = Node(newdata)
#        yeni eklenen düğüme göre öncekileri güncelleme
        newnode.next = self.head
        self.head = newnode

    def AddBetween(self,middle_node,newdata):
        if middle_node is None:
            print("Düğüm yok")
            return None
        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode
    def Remove(self,remove):
        head = self.head
        if head is not None:
            if head.data == remove:
                self.head = head.next
                head = None
                return None
        while head is not None:
            if (head.data == remove):
                break
            prev = head
            head = head.next
            
        if head == None:
            return None
        prev.next = head.next
        head = None
        
lst = LinkedList()
lst.head = Node("liste")
a1 = Node("1")
a2 = Node("2")
a3 = Node("3")
a4 = Node("4")
# düğümleri oluşturduk, şimdi ard arda bağlamamız gerekiyor..
lst.head.next = a1
a1.next = a2
a2.next = a3
a3.next = a4

lst.AddBetween(lst.head.next,"k")
lst.Remove("4")
lst.ListPrint()        