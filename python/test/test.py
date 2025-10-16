
def outer(x):
    def inner():
        print(x)

    return inner()

print(outer(10))