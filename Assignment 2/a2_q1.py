from csp import * 
import random
#Question 1



#create an empty dictionary with given size
def rand_graph(p,n):
	graph = {}
	for i in range(n):
		graph.setdefault(i,[])


	#print(graph)
	#Loop through each number and see if we add it to the list, duplicates will be created
	for i in range(n-1):
		for j in range(i,n):
			if i !=j:
				x = random.random()
				#print(x)
				if x <= p:
					graph[i].append(j)
					graph[j].append(i)
			else:
				continue
	return graph




#x = rand_graph(0.1, 105)
#print(x)