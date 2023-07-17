"""CQ10 - List References"""

a:list[str] = ["one"]
b:list[str] = a
a.append("two")

print(b[1])
    # prints "two"
