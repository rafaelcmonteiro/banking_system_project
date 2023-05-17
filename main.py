from bank import Bank
if __name__ == '__main__':
    new_bank_account = Bank("Rafael", 27, "Male")
    new_bank_account.deposit(1)
    new_bank_account.show_details()
    new_bank_account.withdraw(2)
    new_bank_account.view_balance()