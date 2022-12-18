a = list(eval(input()))
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a) #Сложность O(2n)

b = list(eval(input()))
print(sorted(b)) #Сложность O(2n)