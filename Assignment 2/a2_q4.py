from csp import * 
from a2_q1 import * 
from a2_q2 import *
import time




def constraints(A,a,B,b):
	return a != b 


#calculating the number of teams theyre divided into
def calculate_team(final):
	teams_num = []
	#loop through the different values, if its new add it to team_nums
	for i in range(len(final)-1):
		if final[i] not in teams_num:
			teams_num.append(final[i])
	return len(teams_num)

#Creating csp object, need variables (nodes), domain (possible values) and neighbors.
def calculate_stats(graph):
	variables = []
	domain = {}
	neighbors = graph

	total_assign = 0
	total_unassign = 0


	#print("This is what the graph looks like: ", graph)
	##AC3 sets constraints and removing some parts of the domain backtracking_search gives the solution.
	##

	for keys in graph:
		variables.append(keys)
	new_d = []
	for i in range(len(variables)):
		new_d.append(i)
		for j in range(len(variables)):
			domain[j] = new_d

	csp_obj = CSP(variables, domain, neighbors, constraints)
	assignment = min_conflicts(csp_obj,1000)
	total_assign = csp_obj.nassigns
	total_unassign = csp_obj.una
	return assignment, total_assign, total_unassign


#TESTING calculate_stats	
#calculate_stats(g)
#g = {0: [4, 7], 1: [3, 6], 2: [9], 3: [1, 6], 4: [0, 5],
#	5: [4], 6: [1, 3], 7: [0], 8: [], 9: [2]}

def run_q4():
	probability = [0.1,0.2,0.3,0.4,0.5,0.6]

	for i in range(6):
		print("-------------------------------------This is the results when the p is ", probability[i], " ---------------------------------")
		for j in range(5):
			graphs = [rand_graph(0.1, 105), rand_graph(0.2, 105), rand_graph(0.3, 105),
            	rand_graph(0.4, 105), rand_graph(0.5, 105), rand_graph(0.6, 105)]
			start = time.time()
			a,b,c = calculate_stats(graphs[i])
			total = time.time() - start

			#print("This is the current assignment: ", a)
			print("Number of teams assigned:", calculate_team(a))
			print("Total time taken:", total)
			print("Total number of times CSP variables were assigned: ", b)
			print("Total number of times CSP variables were unassigned: ", c)
	
			print("===================================================================================================================================")


#test =  {15: 0, 14: 1, 26: 0, 8: 1, 4: 2, 3: 2, 30: 1, 18: 0, 0: 0, 24: 1, 20: 0, 11: 0, 25: 2, 29: 0, 12: 1, 6: 0, 1: 1, 2: 0, 28: 1, 13: 1, 27: 2, 17: 0, 9: 0, 16: 0, 10: 1, 22: 0, 21: 0, 23: 0, 7: 0, 5: 0, 19: 0} 
run_q4()