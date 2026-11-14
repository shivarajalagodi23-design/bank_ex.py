
def deposit(balance, amount):
    return balance + amount


def withdraw(balance, amount):
    if balance - amount >= 1000:
        return balance - amount
    else:
        raise ValueError("Minimum balance of 1000 must be maintained")


if __name__ == "__main__":

    initial_balance = float(input("Enter initial balance: "))

    deposit_amount = float(input("Enter amount to deposit: "))
    total_balance = deposit(initial_balance, deposit_amount)

    print("Total amount after deposit is:", total_balance)

    withdraw_amount = float(input("Enter amount to withdraw: "))

    try:
        total_balance = withdraw(total_balance, withdraw_amount)
        print("Amount after withdrawal is:", total_balance)
    except ValueError as e:
        print("Withdrawal not allowed!", e)
        print("Available balance is:", total_balance)

