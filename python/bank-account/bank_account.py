import threading

class BankAccount:
    def __init__(self):
        self.status = "close"
        self.lock = threading.Lock()

    def get_balance(self):
        if self.status == "open":
            return self.balance
        else:
            raise ValueError("Account is closed")

    def open(self):
        if self.status == "close":
            self.status = "open"
            self.balance = 0
        else:
            raise ValueError("Account is already open")

    def deposit(self, amount):
        if amount <= 0 or self.status == "close":
            raise ValueError("Account is closed")
        self.lock.acquire()
        self.balance += amount
        self.lock.release()

    def withdraw(self, amount):
        if amount <= 0 or self.status == "close":
            raise ValueError("account is closed")
        
        if amount > self.get_balance():
            raise ValueError("withdraw amount greater than balance")
        self.lock.acquire()
        self.balance -= amount
        self.lock.release()

    def close(self):
        if self.status == "open":
            self.status = "close"
            self.balance = 0
        else:
            raise ValueError("Account is already closed")
