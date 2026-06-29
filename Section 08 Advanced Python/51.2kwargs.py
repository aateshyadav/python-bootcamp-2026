def marks(**kwargs):

    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(shubham=34, vikrant=54, jack=34, marie=90, priya=45)