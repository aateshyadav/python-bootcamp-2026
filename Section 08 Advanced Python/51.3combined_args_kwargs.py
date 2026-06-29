def func1(*args,**kwargs):
    print(args)       # output in form  of tuples
    print(kwargs)     # output in form  of dictionary

func1(1, 2, 4, 5, jack=34, jill=32, marie=31)