# class MyStack:
#     def __init__(self,maxstk):
#         self.maxstk=maxstk
#         self.stack=[]
#         self.tos=-1

#     def push(self,item):
#         if self.tos==self.maxstk-1:
#             print("overflow")
#         else:
#             self.tos=self.tos+1
#             self.stack.append(item)
#             print("item pushed:",self.stack)

#     def pop_item(self):
#         if self.tos==-1:
#             print("underflow")
#             return
#         else:
#             temp=self.stack.pop()
#             self.tos=self.tos-1
#             return temp  
        
#     def top_element(self):
#         if self.tos==-1:
#             print("stack is empty")
#         else:
#             print("top element in the stack is:", self.stack[self.tos])


#     def get_min(self):
#         if self.tos == -1:
#             print("stack is empty")
#         else:
#             min_element = self.stack[0]
#             for i in range(1, len(self.stack)):
#                 if self.stack[i] < min_element:
#                     min_element = self.stack[i]
#             print("minimum element in the stack is:", min_element)
    
#     def get_info(self):
#         print("stack=",self.stack,",","tos=",self.tos)

# x=MyStack(5)
# x.push(10)
# x.push(20)
# x.push(30)
# x.push(45)
# p=x.pop_item()
# print("popped item is:",p)
# x.top_element()
# x.get_min()
# x.get_info()

