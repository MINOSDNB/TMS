from functools import wraps


def my_decorator(func):
    """
    эта очень важная функция my_decorator
    """

    @wraps(func)
    def inner(name, age):
        print("decorator hello")
        result = func(name, age)
        print('decorator bye')
        return result

    return inner


@my_decorator
def my_func(name, age):
    """эта очень важная функция my_func
    """
    print(f'hello {name}')
    return age


# a = my_decorator(my_func)


s = my_func("Boris", 50)

print(s)
