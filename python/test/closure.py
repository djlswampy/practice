
def double(x):
    return x * 2

d = double


def outer(x):
    def inner():
        print(x)

    return inner()

