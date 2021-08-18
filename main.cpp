#include <iostream>
#include <stdio.h>
#include <vector>
#include "reversi.cpp"
//#include "mcts.h"

using namespace std;

int main() {
	reversi game;
	bool player = true;
	vector<pair<int, int>> moves;
	pair<int, int> ai_move;
	int copy_board[8][8] = {};

	int row, col;
	int score[3];

	game.boardPrint();
	// for (int row = 0; row < 8; row++) {
	// 	for (int col = 0; col < 8; col++) {
	// 		if ((row == 3 && col == 3) ||(row == 4 && col == 4)) {
	// 			copy_board[row][col] = 1;
	// 		}
	// 		else if ((row == 3 && col == 4) || (row == 4 && col == 3)) {
	// 			copy_board[row][col] = 0;
	// 		}
	// 		else {
	// 			copy_board[row][col] = -1;
	// 		}
	// 	}
	// }

	//for (int i =0; i< 100; i++){
	
	while (!game.gameOver()) { //while statement should keep going until game is done
		if (player) {
			//puts("Player 1's Turn");
			//cin >> row >> col;
			
			puts("It is the Evas (WHITE) turn");
			ai_move = game.evaporation(game.valid_moves(player), player);
			row = ai_move.first;
			col = ai_move.second;
			printf("Eva picked position (%d,%d). \n",row, col);
			
		}
		else {

			puts("It is the MCTS (BLACK) turn");
			// puts("Player 1's Turn");
			// cin >> row >> col;
			//start timer
			ai_move = game.mcts(game.valid_moves(player), player);
			//end timer
			row = ai_move.first;
			col = ai_move.second;
			printf("MCTS picked position (%d,%d). \n",row, col);
   			
		}

		if(row != -1){
			game.play(row, col, player);
		}
		player = !player;
		game.boardPrint();
	}
	int eva = game.mypoints(true);
	int monte = game.mypoints(false);
	if (eva > monte){
		printf("The score is: %d - %d Eva won!!!! \n", (64- monte), monte);
		score[0] += 1;
	}
	else if(monte> eva){
		printf("The score is: %d - %d MCTS won!!!!\n", eva, (64- eva));
		score[1] += 1;
	}
	else{
		printf("It is a draw!!!\n");
		score[2] += 1;
	}
	game.reset(copy_board);
//}
	//printf("The results are: %d - %d - %d \n", score[0], score[1], score[2]);
	return 0;
}
/*
moves = game.valid_moves(player);
	for (int i = 0; i < moves.size(); i++) {
		cout << moves[i].first << "," << moves[i].second << endl;
	}
*/