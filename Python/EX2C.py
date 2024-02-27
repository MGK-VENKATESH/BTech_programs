print("the prime numbers lessthan 20 are:")
l=20
for num in range(l):
    if num>1:
        for i in range(2,num):
            if num%i == 0:
                break
        else:
            print(num)