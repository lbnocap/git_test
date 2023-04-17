def my_yield1():
    a, i = "yield", 0
    while True:
        print("before #{}".format(i), end=",")
        yield a, i
        print("after #{}".format(i), end=",")
        i += 1


def my_yield2():
    a, i = "yield_a", 0
    b, i = "yield_b", 0
    while True:
        print("before #{}".format(i), end=",")
        yield a, i
        yield b, i
        print("after #{}".format(i), end=",")
        i = i + 1


it1 = iter(my_yield1())
it2 = iter(my_yield2())
for i in range(10):
    print("${}".format(i),end=":")
    print(next(it1))
print("\n")
for i in range(10):
    print(next(it2), end=":")
print("this is git test")