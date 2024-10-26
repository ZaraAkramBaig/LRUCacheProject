# # def main():
# #     print("Hello, World!")

# # if __name__ == "__main__":
# #     main()

class Stack:
    def __init__(self,maxstk):
        self.maxstk=maxstk
        self.stack=[]
        self.tos=-1
    def get_info(self):
        print("stack=",self.stack,",","tos=",self.tos)
    def push(self, item):
        if self.tos==self.maxstk-1:
            print("overflow")
        else:
            self.tos=self.tos+1
            self.stack.append(item)
            print("pushed item", self.stack)
    def pop(self):
        if self.tos==-1:
            print("underflow")
            return
        else:
            temp=self.stack.pop()
            self.tos=self.tos-1
            return temp   
    def top_element(self):
        if self.tos==-1:
            print("stack is empty")
        else:
            print("top element=",self.stack[self.tos])
    def is_empty(self):
        if self.tos==-1:
            print("stack is empty")
        else:
            print("stack is not empty")
    def is_full(self):
        if self.tos==self.maxstk-1:
            print("stack is full")
        else:
            print("stack is not full")

s1=Stack(5)
x=4
z=0
y=x+1
s1.push(y)
s1.push(y+1)
s1.push(x)
y=s1.pop()
x=y+1
s1.push(x)
s1.push(z)
while s1.tos != -1:
    z = s1.pop()
    print(z)

print("x=", x)
print("y=", y)
print("z=", z)

s1.get_info()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push('a')
s1.push('b')
s1.get_info()
popped=s1.pop()
print("popped item=",popped)
s1.get_info()
s1.top_element()
s2=Stack(3)
s2.push(100)
s2.push(200)
s2.push(300)
s2.get_info()
s2.top_element()
s1.is_empty()
s2.is_empty()
s1.is_full()

# class ListNode:
#     def __init__(self, data):
#         self.data=data
#         self.next=None

    # def search(self,target):
    #     a=self
    #     if a.data==target:
    #         return [True,None,a]
    #     b=a.next
    #     while b.next is not None and b.data!=target:
    #         a=a.next
    #         b=b.next
    #     return[b is not None,a,b]
    
# x=ListNode(10)
# class ListNode:
#     def __init__(self, data):
#         self.data=data
#         self.next=None
#     def insert(self,data):
#         newnode=ListNode(data)
#         newnode.next=self.next
#         self.next=newnode
#     def buildlist():
#         val=[]
#         a=ListNode(val[0])
#         b=a
#         while True:
#             values=int(input("enter a value"))
#             val.append(values)
#             response=str(input("do you want to add more values/n enter yes or no"))
#             if response=="no":
#                 break
#             b.insert(values)
#             b=b.next
#         return a

# class ListNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#     def insert(self, data):
#         """Inserts a new node with the given data at the beginning of the linked list."""
#         newnode = ListNode(data)
#         newnode.next = self.next
#         self.next = newnode
#     @staticmethod
#     def buildlist():
#         """Builds a linked list interactively, prompting the user for input."""
#         val = []  # Empty list to store values
#         head = None  # Initialize head as None

#         while True:
#             value = int(input("Enter a value: "))
#             val.append(value)

#             response = str(input("Do you want to add more values? (yes/no): ")).lower()
#             if response != "yes":
#                 break

#             # Create the first node if the list is empty
#             if head is None:
#                 head = ListNode(val[0])

#             # Insert subsequent nodes at the beginning using insert()
#             head.insert(value)

#         return head

# # Example usage
# my_list = ListNode.buildlist()
# # Print the linked list (implementation not provided in the prompt)


