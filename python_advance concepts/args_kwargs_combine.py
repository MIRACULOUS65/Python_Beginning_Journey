def func1(*args, **kwargs):
    print("*args:", args)
    print("**kwargs:", kwargs)

func1(1, 2, 3, a=4, b=5)