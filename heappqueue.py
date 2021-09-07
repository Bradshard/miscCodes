from HeapPriorityQueue import HeapPriorityQueue
import random
import matplotlib.pyplot as plt
import pandas as pd
import time

def test_heap(n):
	measures = []
	summa = 0
	a = HeapPriorityQueue()
	sample = random.sample(range(1, 1000*n), n)
	for i in range(n):
		for ele in sample:
			a.add(i,ele)

	for i in range(n):
		start = time.time()
		a.remove_min()
		end = time.time() # nanoseconds
		measures.append(end-start)

	for i in measures:
		summa += i 

	return (n,summa/len(measures),max(measures))

def report_results():
	result_list = []
	for i in range(10000,1000001, 10000):
		result_list.append(test_heap(i))

	return result_list

result_list = report_results()
df = pd.DataFrame(result_list, columns = ['n', 'avg', 'max'])
print(df)
df.plot(x ='n', y='avg', kind = 'line')
df.plot(x ='n', y='max', kind = 'line')
plt.show()
