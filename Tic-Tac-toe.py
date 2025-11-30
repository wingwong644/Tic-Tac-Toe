grid = [["□", "□", "□"],
        ["□", "□", "□"],
        ["□", "□", "□"]]

positions = {
    1: [0, 0], 2: [0, 1], 3: [0, 2],
    4: [1, 0], 5: [1, 1], 6: [1, 2],
    7: [2, 0], 8: [2, 1], 9: [2, 2]
}

def player_turn(move):
    row, col = positions.get(move, (None, None))
    if row is None or grid[row][col] != "□":
        print("Invalid move. Try again.")
        return player_turn(int(input("Enter your move (1-9): ")))
    else:
        grid[row][col] = "X"

def opponent_turn(opp_move):
    row, col = positions.get(opp_move, (None, None))
    if row is None or grid[row][col] != "□":
        print("Invalid move. Try again.")
        return player_turn(int(input("Enter your move (1-9): ")))
    else:
        grid[row][col] = "O" 

def check_winner():
    for row in grid:
        if row[0] == row[1] == row[2] != "□":
            return True
    for col in zip(*grid):
        if col[0] == col[1] == col[2] != "□":
            return True
    if grid[0][0] == grid[1][1] == grid[2][2] != "□":
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] != "□":
        return True
    return False

def is_draw():
    for row in grid:
        if "□" in row:
            return False
    return True

def main():
    print("Player 1 is X and Player 2 is O")
    while True:
        move = int(input("Enter your move (1-9): "))
        player_turn(move)
        for row in grid:
            print(row)
        if check_winner():
            print("Player 1 (X) wins!")
            break
        if is_draw() == True:
            print("It's a draw!")
            break
        opp_move = int(input("Enter opponent's move (1-9): "))
        opponent_turn(opp_move)
        for row in grid:
            print(row)
        if check_winner():
            print("Player 2 (O) wins!")
            break
        if is_draw() == True:
            print("It's a draw!")
            break
        

main()
