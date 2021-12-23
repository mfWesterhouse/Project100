class Atm:
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number
    def CashWithdrawl(self, card_number, pin_number):
        print("Money Withdrawled")
    def BalanceEquiry(self, card_number):
        print("Balanced Checked")
    def CashInput(self, card_number, pin_number):
        print("Money Put In")
account = Atm("1234", "4321")
print(account.card_number)
account.CashWithdrawl("1234", "4321")