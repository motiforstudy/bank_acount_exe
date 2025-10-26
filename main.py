from BankAccount import BankAccount



def manege_acount( holder : str, start_amount : float):

    create_acount = BankAccount(holder, start_amount)

    return create_acount


count_1 = manege_acount("moti", 100000)
count_2 = manege_acount("meni", 200000)

print (count_1.__str__())
print (count_2.__str__())

transfer_money = count_2.transfer_funds(count_1,  500)

print (count_1.__str__())
print (count_2.__str__())