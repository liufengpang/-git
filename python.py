import time


def f1():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{} * {} = {}'.format(j, i, j * i), end='\t')
        print()


def f3(f):
    time1 = time.time()

    def inner():
        f()
        print(time.time() - time1)

    return inner


@f3
def f2():
    for i in range(1, 10):
        time.sleep(1)


f2()
