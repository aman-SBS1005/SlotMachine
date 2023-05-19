import random 

MAX_LINES = 3 # writing it in caps makes it unchangabl(constant)
MAX_BET = 10000
MIN_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
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
                winning_lines.append(line +1)

    return winnings, winning_lines


def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] # this coipes the all_symbols object without changing the all_symbol elements
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = int(input("Enter the amount you would like to deposit Rs"))
        if amount > 0:
            break
        else:
            print("Amount should be greater then 0.")
    return amount


def get_number_of_lines():
    while True:
        lines = int(input("Enter the nuber of lines to bet on (1-" + str(MAX_LINES) + ")? "))
        if 1 <= lines <= MAX_LINES:
            break
        else:
            print("Enter valid number of lines.")
    return lines


def get_bet():
    while True:
        amount = int(input("Enter the amount you would like to Bet on each line Rs"))
        if MIN_BET <= amount <= MAX_BET:
            break
        else:
            print(f"Amount must be between Rs{MIN_BET} - Rs{MAX_BET}.")
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet >balance:
            print(f"You do not have enough to bet that amount, your current balance is Rs{balance}")
        else:
            break

    print(f"You are betting Rs{bet} on {lines} lines. Your Total bet is: Rs{total_bet}")
    
    slots = get_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won Rs{winnings}.")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is Rs{balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with Rs{balance}")

main()