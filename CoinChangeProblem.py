def count_change(money, coins):
    return total(money, coins, 0)

def total(moneyLeft, coins, coinPositionInList):
    # if to less money left its incorrect answer
    if moneyLeft < 0:
        return 0
    # if we achieve to find out exact sum of given coins for given amount the result is 0 which is correct
    if moneyLeft == 0:
        return 1
    # if we are out of coins and we have still money it's also incorrect answer
    if coinPositionInList == len(coins) and moneyLeft > 0:
        return 0
    #left function decrease amount of money for specific coin and right function move to next coin in list
    return total(moneyLeft - coins[coinPositionInList], coins, coinPositionInList) \
           + total(moneyLeft, coins, coinPositionInList + 1)


# Write a function that counts how many different ways you can make change for an amount of money, given an array of coin denominations. For example, there are 3 ways to give change for 4 if you have coins with denomination 1 and 2:
#
# 1+1+1+1, 1+1+2, 2+2.
# The order of coins does not matter:
#
# 1+1+2 == 2+1+1
# Also, assume that you have an infinite amount of coins.
#
# Your function should take an amount to change and an array of unique denominations for the coins:
#
#   count_change(4, [1,2]) # => 3
#   count_change(10, [5,2,3]) # => 4
#   count_change(11, [5,7]) # => 0