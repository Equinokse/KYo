a = list(eval(input())) #Сложность O(3n)
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)
b = a
for c in range(len(b)-1):
    for x in range(len(b)-c-1):
        if b[x+1] > b[x]:
            b[x], b[x+1] = b[x+1], b[x]
print(b)