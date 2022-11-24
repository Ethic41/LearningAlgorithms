#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-07-09 01:27:33
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : https://www.codechef.com/JULY221D/problems/KNIGHT2
# @Version : 1.0.0


def solve():
    def knight_move(X1: int, Y1: int, X2: int, Y2: int):
        start = X1, Y1
        end = X2, Y2
        
        def generate_board(X1: int, Y1: int, X2: int, Y2: int):
            board = [['0' for _ in range(8)] for _ in range(8)]
            board[X1][Y1] = "S"
            board[X2][Y2] = "E"
            return board
        
        def get_valid_moves(X: int, Y: int):
            valid_moves = []
            if is_valid(X + 1, Y + 2):
                valid_moves.append((X + 1, Y + 2))
            if is_valid(X - 1, Y + 2):
                valid_moves.append((X - 1, Y + 2))
            if is_valid(X + 2, Y + 1):
                valid_moves.append((X + 2, Y + 1))
            if is_valid(X - 2, Y + 1):
                valid_moves.append((X - 2, Y + 1))
            
            if is_valid(X + 1, Y - 2):
                valid_moves.append((X + 1, Y - 2))
            if is_valid(X - 1, Y - 2):
                valid_moves.append((X - 1, Y - 2))
            if is_valid(X + 2, Y - 1):
                valid_moves.append((X + 2, Y - 1))
            if is_valid(X - 2, Y - 1):
                valid_moves.append((X - 2, Y - 1))
            
            return valid_moves
        

        def is_valid(X: int, Y: int):
            if 0 <= X < 8 and 0 <= Y < 8:
                return True

            return False 

        
        def print_board(board: list):
            for row in board:
                print(row)
        
        def print_board_possible_moves(board: list, moves: list):
            for move in moves:
                board[move[0]][move[1]] = "X"
            print_board(board)
        
        def check_at_destination(pos: tuple):
            if pos == end:
                return True
        
        board = generate_board(X1, Y1, X2, Y2)
        possible_moves = get_valid_moves(X1, Y1)

        # print(possible_moves)
        # print_board_possible_moves(board, possible_moves)


    T = int(input())

    for _ in range(T):
        X1, Y1, X2, Y2 = [*map(int, input().split())]
        print(knight_move(X1-1, Y1-1, X2-1, Y2-1))


if __name__ == "__main__":
    solve()

