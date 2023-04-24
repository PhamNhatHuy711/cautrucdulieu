def uscln(a, b):
    if (b == 0):
        return a
    return print(uscln(b, a % b))
uscln(28,16)