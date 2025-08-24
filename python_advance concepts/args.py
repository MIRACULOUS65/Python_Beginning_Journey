# def sum(a,b):
#     return a+b

def sum(*args):
    #ARGS WILL BE A TUPLE OF ALL THE VALUES PASSED IN THE FUNCTION
    total=0
    for i in args:
        total+=i
    return total

print(sum(2,3,7))