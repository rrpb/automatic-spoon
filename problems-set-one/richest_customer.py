"""You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth."""


def get_max_wealth(accounts) -> int:
    current_sum, max_sum = 0, 0
    for account in accounts:
        current_sum = sum(account)
        max_sum = max(current_sum, max_sum)
    return max_sum

accounts = [[1,2,3],[3,2,1]]
print(get_max_wealth(accounts))