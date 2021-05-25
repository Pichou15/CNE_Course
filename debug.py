def lone_sum(a, b, c):
    sum = 0
    if a == b and a ==c and b == c:
        return 0
    elif b == c:
        return a
    elif a == c:
        return b
    elif a == b:
        return c
    else:
        return a + b + c


sum = lone_sum(1, 2, 3)
print(sum)
        

