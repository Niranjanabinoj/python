st=input("enter a string:")
n=len(st)
pt=st
if st[:n]==pt[n::-1]:
    print("palindrome")
else:
    print("not palindrome")
