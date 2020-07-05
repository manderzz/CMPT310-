from csp import * 
from a2_q1 import * 
import time

"""
I have added in a variable called una to keep track of the number of unassigned CSP variables, and also added an additional line in the unassigned method, 
that counts the number of unassigned CSP variables, please make this change in csp.py.
class CSP(search.Problem):

    def __init__(self, variables, domains, neighbors, constraints):
        Construct a CSP problem. If variables is empty, it becomes domains.keys().
        super().__init__(())
        variables = variables or list(domains.keys())
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints
        self.curr_domains = None
        self.nassigns = 0
        self.una = 0   ######to keep track how many variables are unassigned 

    def unassign(self, var, assignment):
        Remove {var: val} from assignment.
        DO NOT call this if you are changing a variable to a new value;
        just call assign for that.
        if var in assignment:
            del assignment[var]
            self.una +=1 ###########  added in


"""
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
	#domain = {0:[0,1,2,3], 1:[0,1,2,3],2:[0,1,2,3],3:[0,1,2,3]}
	neighbors = graph

	total_assign = 0
	total_unassign = 0


	##AC3 sets constraints and removing some parts of the domain backtracking_search gives the solution.
	##

	for keys in graph:
		variables.append(keys)
	##start time
	for i in range(len(variables)):
		domain.append(i)

		csp_obj = CSP(variables, domain, neighbors, constraints)
		#AC3(csp_obj)

		print(domain)
		
		assignment = backtracking_search(csp_obj, mrv, lcv, forward_checking)
		total_assign += csp_obj.nassigns
		total_unassign += csp_obj.una

		#number of assignments made to reach the solution 
		current = csp_obj.nassigns

		#print("This is after backtracking_search")
		#csp_obj.display(assignment)
		#print(total_assign)
		#print(total_unassign)

		if assignment != None:
			break
	return assignment, total_assign, total_unassign, current


#TESTING calculate_stats	
#calculate_stats(g)
#g = {0: [4, 7], 1: [3, 6], 2: [9], 3: [1, 6], 4: [0, 5],
#	5: [4], 6: [1, 3], 7: [0], 8: [], 9: [2]}

def run_q3():
	probability = [0.1,0.2,0.3,0.4,0.5,0.6]

	for i in range(1):
		print("-------------------------------------This is the results when the p is ", probability[i], " ---------------------------------")
		for j in range(1):
			graphs = [rand_graph(0.1, 31), rand_graph(0.2, 31), rand_graph(0.3, 31),
            	rand_graph(0.4, 31), rand_graph(0.5, 31), rand_graph(0.6, 31)]
			start = time.time()
			a,b,c, d= calculate_stats(graphs[i])
			total = time.time() - start
			print("The graph with corresponding edges: ", graphs[i])
			print("Number of teams assigned:", calculate_team(a))
			print("Total time taken:", total)
			print("Total number of times CSP variables were assigned: ", b)
			print("Total number of times CSP variables were unassigned: ", c)
			print("This is number of assigned to reach the solution: ", d)
	
			print("===================================================================================================================================")


#test =  {15: 0, 14: 1, 26: 0, 8: 1, 4: 2, 3: 2, 30: 1, 18: 0, 0: 0, 24: 1, 20: 0, 11: 0, 25: 2, 29: 0, 12: 1, 6: 0, 1: 1, 2: 0, 28: 1, 13: 1, 27: 2, 17: 0, 9: 0, 16: 0, 10: 1, 22: 0, 21: 0, 23: 0, 7: 0, 5: 0, 19: 0} 
#run_q3()


calculate_stats(rand_graph(0.1,31))