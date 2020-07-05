# CMPT 310 - Artificial Intelligence 

Exploring different topics of articifial intelligence, used aima-python repository for some external code.

## Assignment 1

Compared the efficiency of A* search using misplaced tile heursitics (aima-python implementation) and A* search using Manhattan distance heuristics (own implementation) to see which would solve the 8-puzzle more quickly (less time) and effectively (least number of moves).
In each heuristic, the total running time (seconds), number of tiles moved (length of solution) and total number of nodes that were removed from *frontier* were all recorded. 

## Assignment 2

The Ice Breaker Problem: given a group of n people, what is the **minimum** nunmber of teams they can be partitioned into such that no team has 2 (or more) memebers who are friends. In this assignment a team can consists of a single person in it.

## Assignment 3 
A tic-tac-toe game where the AI makes decisions by doing random playouts, record the results of win/loss/draw and choses the move that resulted in the greatest number of wins.

THe idea is to perform enough random playouts so the AI **never loses** against a smart player. Monte-Carlo-Tree Search(Selection, Expansion, Simulation, Back Propagation) was used for random playouts, you start with some board and select the step you want to simulate, then expand  until win/loss/draw, simulate by performing random legal moves and back propagate back to the original board.


