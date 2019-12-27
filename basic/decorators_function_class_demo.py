def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(*args)
        print(**kwargs)
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display():
    print('display function ran')


@decorator_function
def display_info(first, last):
    print('information {} {} is printed'.format(first, last))


display_info('anand', 'raju')
display()

