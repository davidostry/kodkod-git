1.
count = 0
def dump():
    global count
    count +=1
def value():
    return count
dump()
dump()
dump()

2.
def make_counter():
    count = 0
    def inner():
        nonlocal count
        count +=1
        return count
    return inner
c = make_counter()

print(c())
print(c())
print(c())
# 3.
# x = "global"
# def outer():
#     x = "enclosing"
#     def inner():
#         x = "local"
#         print(x)
#     inner()
#     print(x)
# outer()
# print(x)
# 4.
# l = [1, 2, 3]
# print(list(range(5)))

