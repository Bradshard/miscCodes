class regulaFalsi:

	def __init__(self, a, b, i, d, e, f, g, max_iter = 100000):
		self.a = a  # lower bound
		self.b = b  # upper bound
		self.max_iter = max_iter  # maximum iteration time
		self.i = i  # give me the function coefficient of zeroth degree value
		self.d = d  # give me coefficient of the first degree of the function
		self.e = e  # give me coefficient of the second degree of the function
		self.f = f  # give me coefficient of the third degree of the function
		self.g = g  # give me coefficient of the fourth degree of the function

	def __int__(self):
		return self.x # ???
    
	@staticmethod
	def func(i, d, e, f, g, x): # functions up to fourth degree

		return (g*x**4 + f*x**3 + e*x**2 + d*x**1 + i) 

	@staticmethod
	def regulaFalsisolver(a, b, i, d, e, f, g):
		if ((regulaFalsi.func(i, d, e, f, g, a) * regulaFalsi.func(i, d, e, f, g, b)) >= 0):
			 # 'int' object has no attribute 'func' how to solve this issue.

			print(" You have not assumed right a and b")
			return -1

		self.c = self.a # Initialize result
		for i in range(self.max_iter):
			# Find the point that touches x axis
			self.c = (self.a * self.func(self.i, self.d, self.e, self.f, self.g,self.b) - self.b * self.func(self.i, self.d, self.e, self.f, self.g, self.a)) / (self.func(self.i, self.d, self.e, self.f, self.g, self.b) - self.func(self.i, self.d, self.e, self.f, self.g, self.a))
		# Check if the above found point is root
			if self.func(self.i, self.d, self.e, self.f, self.g, self.c) == 0:
				break
	# Decide thes side to repeat the steps
			elif self.func(self.i, self.d, self.e, self.f, self.g, self.c) * self.func(self.i, self.d, self.e, self.f, self.g, self.a) < 0:
				self.b = self.c
			else:
				self.a = self.c
		print(" The value of root is : ", '%.4f' %self.c)


regulaFalsi(-200 ,300, 1, 2, 1, 0, 0)
regulaFalsi.regulaFalsisolver(-200, 300, 1, 2, 1, 0, 0)
