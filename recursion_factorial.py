def fact(i):
    if i==0 or i==1:
        return 1
    else:
        return i*fact(i-1)
n=int(input("enter a no"))
factorial=fact(n)
print("factorial is",factorial)
