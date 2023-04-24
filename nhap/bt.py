n = int(input("Nhap so luong day so nguyen: "))
x = []
for i in range(n):
    a = int(input("nhap 1 so nguyen: "))
    x.append(a)
print(x)
print(sorted(x))
m = int(input("Nhap so luong day so nguyen: "))
y = []
z = {}
for i in range(m):
    b = int(input("nhap 1 so nguyen: "))
    y.append(b)
for i in y:
    if i in z:
        z[i] += 1
    else:
        z[i] = 1
for i, j in z.items():
    print(i, j)
