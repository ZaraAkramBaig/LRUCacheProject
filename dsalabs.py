# from timeit import default_timer as timer
# def listsearch(mylist,data):
#     for i in range(len(mylist)):
#         if(mylist[i]==data):
#             print("data is found at positon:", i)
#         else:
#             print("error, element not found!!")
#             break
# #user-defined
# start=timer()
# listsearch([1,2,3,4,45,6,67,667],34,)
# end=timer()
# print("time elapsed by user defined:", end-start)
# #built-in
# start=timer()
# mylist=[1,2,3,4,45,6,67,667]
# index=mylist.index(45)
# print("data is found at positon:", index)
# end=timer()
# print("time elapsed by buitlt-in:", end-start)

# from timeit import default_timer as timer
# def listdelete(mylist,data):
#     for i in range(len(mylist)):
#         if(mylist[i]==data):
#             list1=mylist[0:i]
#             list2=mylist[i+1:len(mylist)]
#             final_list=list1+list2
#             print(final_list)
#         else:
#             print("error, element not found!!")
#             break
# #user-defined
# start=timer()
# listdelete([1,2,3,4,45,6,67,667],34,)
# end=timer()
# print("time elapsed by user defined:", end-start)
# #built-in
# start=timer()
# mylist=[1,2,3,4,45,6,67,667]
# mylist.remove(45)
# print(mylist)
# end=timer()
# print("time elapsed by buitlt-in:", end-start)

from timeit import default_timer as timer
def listinsert(mylist,data,pos):
    element=[data]
    list1=mylist[0:pos]
    list2=mylist[pos:len(mylist)]
    list1=list1+element
    final_list=list1+list2
    print(final_list)
#user-defined
start=timer()
listinsert([1,2,3,4,45,6,67,667],34,4)
end=timer()
print("time elapsed by user defined:", end-start)
#built-in
start=timer()
mylist=[1,2,3,4,45,6,67,667]
mylist.insert(5,78)
print(mylist)
end=timer()
print("time elapsed by buitlt-in:", end-start)




