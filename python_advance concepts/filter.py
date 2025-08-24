# def is_greater_than_5(num):
#     if num>5:
#         return True
#     else:
#         return False
    
a=[1,2,3,4,5,6,7,8,9,10]
b=filter(lambda num:(num>5),a)
print(list(b)) #filter always return filter object but if you want to see the value then you have to convert it into list or tuple
