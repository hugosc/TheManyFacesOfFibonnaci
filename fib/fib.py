def basicFibonacci(n):
	if (n <= 1): 
		return n
	else:
		return basicFibonacci(n-1) + basicFibonacci(n-2)


def linearFibonacci(n):


	memory = [0, 1] + [None] * (n-1)

	def rec(n):
		if n <= 1:
			return n

		if memory[n] == None:
			 memory[n] = rec(n-1) + rec(n-2)
		
		return memory[n]

	return rec(n)