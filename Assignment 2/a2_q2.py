from csp import * 


#question 2
def check_teams(graph, csp_sol):
	for i in range(len(graph)):
		for j in range(i,len(graph)):
			#print("This is the value of i ", i )
			#print("This is the value of j ", j)
			if i !=j:

				##If theyre not on the same team, they are either friends or ALONE. Which means 
				if csp_sol[i] != csp_sol[j]:
					if graph[i]== []:
						break
					if graph[j] == []:
						break
					if graph[i].count(j) < 1:
						#print("First")
						return False
					if graph[j].count(i) <1:
						#print("Second")
						return False
				else:
				#If they are on the SAME team for sure they are not friends, which means if I can find the values in dictionary I return false
					if graph[i].count(j) == 1:
						#print("Third")
						return False
					if graph[j].count(i) == 1:
						#print("Fourth")
						return False
	return True 





#X = {0:0, 1:1, 2:1, 3:0}
#g = {0: [1,2], 1: [0], 2: [], 3: []} 
#answer = check_teams(g,X)
#print(answer)




