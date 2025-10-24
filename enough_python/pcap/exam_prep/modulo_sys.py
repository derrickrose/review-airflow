import sys

print("attributes", len(dir(sys)))
a = 0
for i in dir(sys):
    if callable(getattr(sys, i)):
        print(i, end="|")
        a += 1
    elif i == "path":
        print("path", i)
print()
print("functions", a)
