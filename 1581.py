def myswap(a, b):
    return b, a

a, b = input().split(' ')
a = int(a)
b = int(b)

if a > b:
    a, b = myswap(a, b)

print("{} {}".format(a, b))
