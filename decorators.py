
def compose(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@compose
def sum_them(x, y, z):
    return x ** y*z

@compose
def multiply_them(x, y, z):
    return x * y * z

@compose
def display():
    print('this is the {} module'.format(__name__))

def main():
    print(sum_them(2, 5, 5))
    print(multiply_them(2, 5, 5))
    display()

if __name__ == '__main__': main()