"""
Simple Tic-Tac-Toe playable in the terminal.

Controls: enter a number 1-9 to place your mark on the board:

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Players alternate: `X` goes first, then `O`.
"""

def create_board():
	return [" "] * 9


def print_board(board):
	rows = [board[i:i+3] for i in range(0, 9, 3)]
	lines = []
	for r in rows:
		lines.append(f" {r[0]} | {r[1]} | {r[2]} ")
	print("\n---+---+---\n".join(lines))


def is_valid_move(board, pos):
	return 1 <= pos <= 9 and board[pos - 1] == " "


def get_move(board, player):
	while True:
		try:
			val = input(f"Player {player} - enter position (1-9): ")
			pos = int(val)
		except ValueError:
			print("Invalid input. Enter a number from 1 to 9.")
			continue

		if not is_valid_move(board, pos):
			print("That position is not available. Try again.")
			continue

		return pos - 1


def check_win(board, mark):
	wins = (
		(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
		(0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
		(0, 4, 8), (2, 4, 6),             # diagonals
	)
	for a, b, c in wins:
		if board[a] == board[b] == board[c] == mark:
			return True
	return False


def check_draw(board):
	return all(cell != " " for cell in board)


def switch_player(player):
	return "O" if player == "X" else "X"


def play_game():
	board = create_board()
	current = "X"
	print("Tic-Tac-Toe: X goes first")
	print_board(board)

	while True:
		idx = get_move(board, current)
		board[idx] = current
		print_board(board)

		if check_win(board, current):
			print(f"Player {current} wins!")
			break

		if check_draw(board):
			print("It's a draw!")
			break

		current = switch_player(current)


def main():
	while True:
		play_game()
		again = input("Play again? (y/n): ").strip().lower()
		if again != "y":
			print("Thanks for playing!")
			break


if __name__ == "__main__":
	main()