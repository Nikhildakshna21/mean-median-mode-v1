def median(x):
    a = x
    a.sort()
    if len(a) % 2 == 0:
        return (a[len(a)//2]+a[(len(a)//2)-1])/2

    elif len(a) % 2 == 1:
        return a[len(a)//2]


