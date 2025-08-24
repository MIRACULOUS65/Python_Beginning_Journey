numbers=[1,2,3,4,5,6,7,8,9,10]

# def square(num):
#     return num*num

#here the lambda function is same as the above function
new= map(lambda num:num*num,numbers)#map always return map object but if you want to see the value then you have to convert it into list or tuple

print(list(new))