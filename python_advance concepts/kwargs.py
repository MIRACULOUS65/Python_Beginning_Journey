def marks(**kwargs):
    for items in kwargs.keys():
        print(kwargs[items])
        print(f"{items} has scored {kwargs[items]} marks")

marks(John=90, Smith=78, Alice=88)
#john is the key and 90 is the item value
#means it's a dictionary of key value pairs which is passed in the function