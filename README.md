# CMPT 310 - Artificial Intelligence 

Exploring different topics of articifial intelligence, used aima-python repository for some external code.

## Assignment 1

Compared the efficiency of A* search using misplaced tile heursitics (aima-python implementation) and A* search using Manhattan distance heuristics (own implementation) to see which would solve the 8-puzzle more quickly (less time) and effectively (least number of moves).
In each heuristic, the total running time (seconds), number of tiles moved (length of solution) and total number of nodes that were removed from *frontier* were all recorded. 


## Assignment 3 
A tic-tac-toe game where the AI makes decisions by doing random playouts, which is making random moves for each player until a win, loss, or draw is reached. When a playout is finished, results are recorded (number of wins/loss/draws) and choses the move that resulted in the greatest number of wins.

Objective of the assignment is to perform enough random playouts so our program *never loses* against a smart player. Monte-Carlo-Tree Search(Selection, Expansion, Simulation, Back Propagation) was used for random playouts, since you start with some board and select the step you want to simulate, then expand  until win/loss/draw, simulate by performing random legal moves and back propagate back to the original board.


