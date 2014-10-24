#!/usr/bin/env python3

"""Xs and Os Referee

Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two
players (X and O) who take turns marking the spaces in a 3×3 grid. The
player who succeeds in placing three respective marks in a horizontal,
vertical, or diagonal rows (NW-SE and NE-SW) wins the game.

But we will not be playing this game. You will be the referee for this
games results. You are given a result of a game and you must determine
if the game ends in a win or a draw as well as who will be the
winner. Make sure to return "X" if the X-player wins and "O" if the
O-player wins. If the game is a draw, return "D".

A game's result is presented as a list of strings, where "X" and "O" are
players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).

Output: "X", "O" or "D" as a string.

How it is used: The concepts in this task will help you when iterating
data types. They can also be used in game algorithms, allowing you to
know how to check results.

Precondition:
There is either one winner or a draw.
len(game_result) == 3
all(len(row) == 3 for row in game_result)

"""


def checkio(game_result):

    # A 'win slot' is a triple of co-ordinates where, if a player occupies all three
    # co-ordinates, they have won.  There are eight win slots: three rows, three
    # columns, and two diagonals.  Here we compute those eight win slots.

    row_slots = [[(row, col) for col in range(0, 3)] for row in range(0, 3)]
    col_slots = [[(row, col) for row in range(0, 3)] for col in range(0, 3)]
    dia_slots = [[(i, i) for i in range(0, 3)], [(i, 2 - i) for i in range(0, 3)]]
    win_slots = row_slots + col_slots + dia_slots

    # Now simply check each win slot to see if it contains a win for either party.
    # Although a real game can't have both sides win, a randomly generated board _can_,
    # so we guard against that case by building a set of winners and checking it,
    # rather than just returning the first winner we find.

    winners = set()
    for candidate in win_slots:
        contents = ''.join([game_result[row][col] for (row, col) in candidate])
        for player in 'OX':
            if contents == player * 3:
                winners.add(player)

    if len(winners) == 1:
        return winners.pop()

    # No winner or two winners, so it's a draw
    return 'D'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
