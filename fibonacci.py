n=int(input("enter limit:"))
lb=0
rb=1
print(lb,rb,end=" ")
for i in range(2,n):
    n=lb+rb
    print(n,end=" ")
    lb=rb
    rb=n
