# def mydecordator(function):

#     def wrapper():
#         print("I'm decorating the function")
#         function()
#         #return wrapper

#     return wrapper

# def hello_world():
#     print('Hello World')


# # instead try 

# def mydecordator(function):

#     def wrapper():
#         print("I'm decorating the function")
#         function()
#         #return wrapper

#     return wrapper

# @mydecordator
# def hello(person):
#     print(f"Hello {person}")

# hello('Mike')

# wont work becauase wrapper does not take arguments

def mydecordator(function):

    def wrapper(*args, **kwargs):
        print("I'm decorating the function")
        return function(*args, **kwargs)

    return wrapper

@mydecordator
def hello(person):
    return f"Hello {person}"

print(hello('Mike'))