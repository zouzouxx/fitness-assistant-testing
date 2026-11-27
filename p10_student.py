def calc(a, op, b):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        if b==0:
            return None
        return a/b
    else:
        return None

print(calc(10, "+", 5))
print(calc(10, "/", 0))
print(calc(10, "%", 3))
print(calc(10, "/", 4))
