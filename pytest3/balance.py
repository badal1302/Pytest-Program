def check_balance(amt,withdraw):
    if(withdraw>amt):
        return 'Insufficient amount'
    else:
        return amt-withdraw