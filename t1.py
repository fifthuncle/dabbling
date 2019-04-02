import random
a = [random.randint(1, 10000) for i in range(10000)]
print(a[:5])
print(a[-5:])
a.sort()
print(a[:5])
print(a[-5:])