class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None        # parameters of the class
        self.previous = None

    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = newNode
            self.previous.next = current    #joins previous Node with new Node
            self.previous = current     #previous is a field
        else:
            self.head = newNode
            self.previous = newNode

    def printLL(self):
        current = self.head
        while(current):
          print(current.data)
          current = current.next


    def find(self, number):
        current = self.head
        self.previous = None
        while(current):
            if current.data == number: #if current number is not equal to serached number and if current Node has no following Node
                return current, self.previous       # previous shoulkd be in other place
            elif current.next == None:
                return None
            else:
                self.previous = current
                following = current.next
                current = following


    def replace(self, number):
        searchedNode = LL.find(number)
        if searchedNode == None:
            print('such number was not found')
        else:
            current = searchedNode[0]
            current.data = input("enter new number")

    def delete(self, number):
        searchedNode = LL.find(number)
        if searchedNode == None:
            print('such number was not found')
        else:
            current = searchedNode[0]
            previous = searchedNode[1]
            if previous == None:
                LL.head = current.next
            else:
                previous.next = current.next


LL = LinkedList()

def insertion():
    print("give number, type R to replace, D to delete, P to print or other letter exit")
    number = input()
    if number.isdigit():
        LL.insert(number)
        insertion()
    elif number == "R" or number == "r":
        number = input("enter number to be replaced")
        LL.replace(number)
        insertion()
    elif number == "D" or number == "d":
        number = input("enter number to be deleted")
        LL.delete(number)
        insertion()
    elif number == "P" or number == "p":
        LL.printLL()
        insertion()
    elif number == "E" or number == "e":
        return None
    else:
        print("No such command. Try again")
        insertion()


insertion()