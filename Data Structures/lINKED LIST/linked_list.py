class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp=self.head
        while temp:
            print(temp.data, end="-->")
            temp=temp.next
        print(" ")

    def insertAtHead(self, data):
        new_head=Node(data)
        new_head.next=self.head
        self.head=new_head

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node

    def insertValues(self,data):
        for i in data:
            self.insertAtEnd(i)

    def insertAt(self, data, index):
        new_node = Node(data)
        if index == 0:
            self.insertAtHead(data)
            return
        temp = self.head
        count = 0
        while count < index :
            temp = temp.next
            count += 1
        new_node.next = temp.next
        temp.next = new_node

    def removeAT(self,index):
        if index<0 or index>self.getlength()-1:
            print("Index out of range")
            return
        temp = self.head
        if index == 0:
           self.head = self.head.next
        else:
                count = 1
                while temp:
                    if count == index:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
                    count += 1

    def getlength(self):
        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.next
        return length

    def insert_after_value(self,data_after,data):
        new_node = Node(data)
        temp = self.head
        count=0
        found = False
        while temp:
            if temp.data == data_after:
                found=True
                self.insertAt(new_node.data, count)
            temp=temp.next
            count += 1
        if found:
            print("Insertion completed")
        else:
            print("Insertion failed")

    def remove_by_value(self,data):
        temp = self.head
        count = 0
        found = False
        while temp:
            if temp.data == data:
                found = True
                self.removeAT(count)
            count += 1
            temp = temp.next
        if found:
            print("Value Removed")
        else:
            print("Removing Failed! enter valid value")

if __name__ == '__main__':
    llist = LinkedList()
    llist.insertValues(["banana","mango","grapes","orange"])
    llist.insert_after_value("orange","apple")
    llist.print_list()
    llist.remove_by_value("orange")
    llist.print_list()
    llist.remove_by_value("figs")
    llist.print_list()
    llist.remove_by_value("banana")
    llist.remove_by_value("mango")
    llist.remove_by_value("apple")
    llist.remove_by_value("grapes")
    llist.print_list()


