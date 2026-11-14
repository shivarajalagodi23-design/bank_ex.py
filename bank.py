initial_balance = float(input("Enter initial balance: "))

deposit = float(input("Enter amount to deposit: "))
total_balance = initial_balance + deposit

print("Total amount after deposit is:", total_balance)

withdraw = float(input("Enter amount to withdraw: "))
total_balance = total_balance - withdraw

print("Amount after withdrawal is:", total_balance)
