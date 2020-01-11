class Transaction:
    def __init__(self, name, time, amount, city):
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city
        
class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        transactions = [Transaction(*t.split(',')) for t in transactions]
        transactions.sort(key=lambda t: t.time)
        result = set()
        n = len(transactions)
        for i in range(n):
            t1 = transactions[i]
            if t1.amount > 1000:
                result.add("{},{},{},{}".format(t1.name, t1.time, t1.amount, t1.city))
            for j in range(i + 1, n):
                t2 = transactions[j]
                if t1.name == t2.name and t2.city != t1.city and t2.time - t1.time <= 60:
                    result.add("{},{},{},{}".format(t1.name, t1.time, t1.amount, t1.city))
                    result.add("{},{},{},{}".format(t2.name, t2.time, t2.amount, t2.city))
        return list(result)