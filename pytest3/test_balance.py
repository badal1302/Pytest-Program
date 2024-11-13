from balance import check_balance

def test_sufficient_balance():
    assert check_balance(1000, 500) == 500
    assert check_balance(500, 500) == 0

def test_insufficient_balance():
    assert check_balance(300, 500) == 200
    assert check_balance(0, 100) == 'Insufficient amount'

def test_edge_cases():
    assert check_balance(0, 0) == 0  # No balance, no withdrawal
    assert check_balance(100, 0) == 100  # Withdrawal is zero
    assert check_balance(1, 1) == 0  # Minimal balance and withdrawal
