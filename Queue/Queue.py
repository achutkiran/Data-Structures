class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    #adds element to queue
    def add(self,val):
        node = {"value":val,"next":None}
        if self.tail == None:
            self.head = node
            self.tail = node
        else:
            self.tail["next"] = node
            self.tail = node

    #pops a value from queue
    def pop(self):
        if self.head == None:
            return "Empty Queue"
        else:
            out = self.head
            self.head = self.head["next"]
            return out["value"]

    #prints elements in queue
    def printQueue(self):
        temp = self.head
        while (temp!= None):
            print(temp["value"],end=", ")
            temp = temp["next"]
        print()

#main function
def main():
    queue = Queue()
    while True:
        choice = input("Choose from following options \n1.Add to queue \n2.Pop queue \n3.Print \n4.Quit\nChoice:")
        if choice == "1":
            val = input("Enter value:")
            queue.add(val)
        elif choice == "2":
            val = queue.pop()
            print("Pop value: "+val)
        elif choice == "3":
            queue.printQueue()
        elif choice == "4":
            break
        else:
            print("Enter valid choice")

if __name__=="__main__":
    main()
