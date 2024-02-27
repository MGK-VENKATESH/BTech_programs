def recur_fact(n):
    if n==1:
        return 1
    else:
        return n*recur_fact(n-1)
num=int(input("enter the number for factorial"))
if num<0:
    print("enter valid number")
elif num==0:
    print("the factorial is 1")
else:
    print("the factorial of given number",num,"is",recur_fact(num))