# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 17:44:59 2021

@author: LENOVO
"""
# Node sınıfı temel düğüm yapısı ve elemanlarını oluşturduğumuz kısımdır.
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
# LinledList sınıfı ile ekleme uzunluk hesaplama ve show fonk. yazılmıştır.        
class LinkedList:
    def __init__(self):
        self.head = Node()   
    #append fonk şöyle çalışır:
    # yeni bir düğüm oluşturulur bunun adı new_node
    #baştaki(head) en son girilmiş değerdir(current)-son girilen değer en başta olacağından bunlar eşitlenir.
    #bir sonraki boş olmadığı sürece şeklinde bir loop oluşturulur
    #ve bu döngü içinde şuandaki değer next değere eşitlenir.        
    #ve next değer her zaman yeni düğüm(new_node) olur.                       
    def Append(self,data):
        new_node = Node(data)
        current = self.head
        while current.next!= None:
            current = current.next
        current.next = new_node
    #Length fonksiyonu:
    #şuandaki değer baş a eşittir, ve bir sonraki(next) None olmadığı sürece
    #total değişkeni +1 yapılır. Total değer return edilir.       
    def length(self):
        current = self.head
        total = 0
        while current.next!=None:
            total+=1
            current=current.next
        return total
    #Display fonksiyonu:
    #en son eklenen node head e eşittir ve yine next None olmadığı sürece 
    #boş bir diziye next Node ların dataları(değerleri) eklenir.
    #dizi ekrana yazılır.       
    def Display(self):
        elems = []
        current_node = self.head
        while current_node.next!=None:
            current_node = current_node.next
            elems.append(current_node.data)
        print(elems)
    #getIndex fonksiyonu:
    #Öncelikle index uzunluktan büyük yada eşitse bir hata var demektir ve None return edilir.
    #Ardından başlangıç indexi 0 a eşitlenir ve düğüm de head'e(son değere) eşitlenip başlanır.
    #curret_index(son index) 1 artırılır.            
    def getIndex(self,index):
        if index>=self.length():
            print("ERROR , index out of range!")
            return None
        current_index = 0
        current_node= self.head
        while True:
            current_node= current_node.next
            if current_index == index:
                return current_node.data
            current_index+=1  
    
    def Delet(self,index):
        if index>=self.length():
            print("ERROR ,index out of range")
            return None
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return 
            current_index+=1
            
            
list1 = LinkedList()    
list1.Append(1)
list1.Append(2)
list1.Append(3)
list1.Append(4)
list1.Append(5)
list1.Delet(2)
list1.Display()
print("element at 2nd index:",list1.getIndex(2))
        