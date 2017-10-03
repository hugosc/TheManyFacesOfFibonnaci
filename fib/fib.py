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


def mul2x2(m1, m2):
	return ((m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0], 
		m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1]),
		(m1[1][0]*m2[0][0]+m1[1][1]*m2[1][0],
			m1[1][0]*m2[0][1]+m1[1][1]*m2[1][1]))

def matrixFibonacci(n):


	m = ((1, 1), (1, 0))

	def nthPower(n):

		if n == 1:
			return m

		if n % 2 == 0:
			p = nthPower(n/2)
			return mul2x2(p, p)
		else:
			p = nthPower((n-1)/2)
			return mul2x2(m, mul2x2(p, p))

	if n <= 1:
		return n
	else:
		return nthPower(n)[1][0]
