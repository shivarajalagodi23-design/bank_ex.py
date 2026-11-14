initial_balance = float(input("Enter initial balance: "))

deposit = float(input("Enter amount to deposit: "))
total_balance = initial_balance + deposit

print("Total amount after deposit is:", total_balance)

withdraw = float(input("Enter amount to withdraw: "))
total_balance = total_balance - withdraw

print("Amount after withdrawal is:", total_balance)

if total_balance - withdraw >= 1000:
    total_balance = total_balance - withdraw
    print("Amount after withdrawal is:", total_balance)
else:
    print("Withdrawal not allowed!")
    print("Minimum balance of 1000 must be maintained.")
    print("Available balance is:", total_balance)
