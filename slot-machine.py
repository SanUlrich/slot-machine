import random

MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
	"A": 5,
	"B": 8,
	"C": 11,
	"D": 15,
}

symbol_value = {
	"A": 100,
	"B": 10,
	"C": 3,
	"D": 2,
}


def check_winnings(columns, lines, bet, values):
	"""
	Checks lines in given matrix.
	Returns count of wins and number of winning line.
	"""
	winnings = 0
	winning_lines = []
	for line in range(lines):
		symbol = columns[0][line]
		for column in columns:
			symbol_to_check = column[line]
			if symbol != symbol_to_check:
				break
		else:
			winnings += values[symbol] * bet
			winning_lines.append(line + 1)

	return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
	"""
	From given settings returns the matrix of random symbols.
	"""
	all_symbols = []								# Make a list from given "symbol_count" dict.
	for symbol, symbol_count in symbols.items():
		for _ in range(symbol_count):
			all_symbols.append(symbol)

	columns = []									# Make a matrix ROWS*COLS of random symbols.
	for _ in range(cols):
		column = []
		current_symbols = all_symbols[:]
		for _ in range(rows):
			value = random.choice(current_symbols)
			column.append(value)
			current_symbols.remove(value)

		columns.append(column)

	return columns


def print_slot_machine(columns):
	"""
	Generates and displays the game field.
	"""
	for row in range(len(columns[0])):
		for i, column in enumerate(columns):
			if i != len(columns) - 1:
				print(column[row], end=' | ')
			else:
				print(column[row])


def deposit():
	"""
	The user defines their deposit.
	Returns the amount of the deposited funds.
	"""
	while True:
		amount = input('What is your deposit amount?\n')
		if amount.isdigit():
			amount = int(amount);
			if amount > 0:
				break
			else:
				print('Insufficient funds.\n')
		else:
			print('Invalid input.')

	return amount


def get_number_of_lines():
	"""
	Returns the number of lines on which a bet has been placed.
	"""
	while True:
		lines = input(f'How many lines will you bet on? From 1 to {MAX_LINES}.\n')
		if lines.isdigit():
			lines = int(lines);
			if 1 <= lines <= MAX_LINES:
				break
			else:
				print(f'Need a number from 1 to {MAX_LINES}!\n')
		else:
			print('Invalid input.')

	return lines


def get_bet():
	"""
	Takes a bet from the player. Returns the total amount of the bet.
	"""
	while True:
		bet = input(f'What is your bet per line (from ${MIN_BET} to ${MAX_BET}):\n')
		if bet.isdigit():
			bet = int(bet);
			if MIN_BET <= bet <= MAX_BET:
				break
			else:
				print('Enter an acceptable amount.\n')
		else:
			print('Invalid input.')

	return bet


def game(balance):
	"""
	The function accepts a bet, do a spin
	and returns the player's balance after win or loss.
	"""
	lines = get_number_of_lines()	# Acception of lines.
	while True:
		bet = get_bet()				# Acception a money bet.
		total_bet = bet * lines

		if total_bet > balance:
			print(f'Not enough funds. Your balance: ${balance}.')
		else:
			break

	print(f'Your bet on {lines} lines is ${bet} each. Total bet is ${total_bet}')

	slots = get_slot_machine_spin(ROWS, COLS, symbol_count)		# Spin slot machine.
	print_slot_machine(slots)
	winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
	print(f'You won: ${winnings}')
	print(f'Winning line:', *winning_lines)

	return winnings - total_bet


def main():
	"""
	Main function that starts the game.
	"""
	balance = deposit()
	while True:
		print(f'Now you have ${balance}')
		answer = input('Press Enter to roll (press "q" to exit).')
		if answer == 'q':
			break

		balance += game(balance)

	print(f"You're leaving with ${balance} in your pocket.")

	
if __name__ == "__main__":
	main()
