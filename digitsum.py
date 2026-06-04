n=int(input("enter a no"))
summ=0
while n>0:
    temp=n%10
    summ=summ+temp
    n=n//10
print(summ)
