def hairbrush(a):
    step = len(a) - 1
    while step > 0:
        for i in range(0, len(a)-step):
            if (a[i] > a[i+step]):
                a[i], a[i+step] = a[i+step], a[i]
        step = int(step//1.25)
    return a