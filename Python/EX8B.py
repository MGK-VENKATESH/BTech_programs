import statistics
n=int(input("enter the number of elements"))
lst=[]
for i in range(n):
    x=int(input("enter the elements:"))
    lst.append(x)
print(lst)
mean=statistics.mean(lst)
print("mean of elements:",mean)
median=statistics.median(lst)
print("median of elements:",median)
mode=statistics.mode(lst)
print("mode of given elements:",mode)