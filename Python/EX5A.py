class py_solution:	
					# Python3 program for the above approach
		def power(x, n):
			pow=1

	# Multiply x for n times
			for i in range(n):
				pow = pow * x

			return pow



x = int(input("enter the value of x"))
n = int(input("enter the value of n"))


print(py_solution.power(x, n))
