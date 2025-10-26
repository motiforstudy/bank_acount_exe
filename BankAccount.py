


class BankAccount:
    """
    this class should create a bank acount
    """

    def __init__(self, account_holder : str, initial_balance : float):
        """
        initial the user account
        :param account_holder: the owner of the acount
        :param initial_balance: how much many the owner deposit at the begging
        """
        self.holder = account_holder
        self.balance = initial_balance

    def transfer_funds(self, other_account, amount):
        """
        to make a transfer from one acount to ather
        :param other_account: the other person that we transfer him money
        :param amount: the amount of the transfer
        :return: if the transfer succeeded
        """
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            print ("the transfer went successfully")

        else:
            print ("there is an error")


    def __str__(self):

        return f"acount status: the owner is: {self.holder}. the current balance is: {self.balance}"

