import pytest
from app.calculations import add, sub, mul, div, BankAccount, InsufficientFunds


@pytest.fixture
def zero_bank_account():
    print("Creating an empty bank account")
    return BankAccount()


@pytest.fixture
def bank_account():
    return BankAccount(50)


@pytest.mark.parametrize("num1, num2, expected", 
        [
            (3,2,5),
            (7,1,8),
            (12,4,16),
            (16,4,20)
        ]
    )
def test_add(num1, num2, expected):
    print("Tetsting add function")
    assert add(num1, num2) == expected


def test_bank_set_initial_ammount(bank_account):
    assert bank_account.balance == 50


def test_bank_default_ammount(zero_bank_account):
    assert zero_bank_account.balance == 0


def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30


def test_deposit(bank_account):
    bank_account.deposit(50)
    assert bank_account.balance == (100)

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert int(bank_account.balance) == 55


@pytest.mark.parametrize("deposited, withdraw, expected", 
        [
            (200,100,100),
            (50,10,40),
            (1200,200,1000)
        ]
    )

def test_bank_transaction(zero_bank_account, deposited, withdraw, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdraw)
    assert zero_bank_account.balance == expected

def test_insuff(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)



# def test_sub(num1, num2, expected):
#     print("Tetsting sub function")
#     assert sub(num1, num2) == expected


# def test_div(num1, num2, expected):
#     print("Tetsting div function")
#     assert div(num1, num2) == expected


# def test_mul(num1, num2, expected):
#     print("Tetsting mul function")
#     assert mul(num1, num2) == expected