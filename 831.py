class BalanceError(Exception):
    pass

balance = -100

try :
    if balance < 100 :
        raise BalanceError("Balance cannot be negative")


except BalanceError as Error :
    print(Error) 