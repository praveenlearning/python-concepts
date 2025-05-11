from typing import Optional


def solution(queries):
    b = Bank()
    return list(map(lambda query: b.handle_query(query), queries))


class Transaction:

    def __init__(self, t, timestamp, amount):
        self.t = t
        self.timestamp = timestamp
        self.amount = amount


class Account:
    def __init__(self, timestamp, account_id):
        self.timestamp = timestamp
        self.id = account_id
        self.balance = 0
        self.transactions = []

    def deposit(self, timestamp, amount):
        self.balance += amount
        return str(self.balance)

    def pay(self, timestamp, amount):
        if self.balance < amount:
            return ""

        self.balance -= amount
        return str(self.balance)


class Bank:
    def __init__(self):
        self.accounts = []
        self.transactions = {}

    def handle_query(self, query):
        T, *args = query

        return getattr(self, T.lower())(*args)

    def get_account(self, account_id) -> Optional[Account]:
        return next(filter(lambda x: x.id == account_id, self.accounts), None)

    def create_account(self, timestamp, account_id) -> str:
        account = self.get_account(account_id)
        if not account:
            self.accounts.append(Account(timestamp, account_id))
            return "true"

        return "false"

    def deposit(self, timestamp, account_id, amount):
        account = self.get_account(account_id)
        if not account:
            return ""

        value = self.transactions.get(account_id, 0)
        self.transactions[account_id] = value + int(amount)
        return account.deposit(timestamp, int(amount))

    def pay(self, timestamp, account_id, amount) -> str:
        account = self.get_account(account_id)
        if not account:
            return ""

        value = self.transactions.get(account_id, 0)
        self.transactions[account_id] = value + int(amount)
        return account.pay(timestamp, int(amount))

    def top_activity(self, timestamp, n):
        txns = dict(sorted(self.transactions.items(), key=lambda x: x[1], reverse=True)[:int(n)])

        return list(map(lambda x: f"{x[0]}({x[1]})", txns.items()))
