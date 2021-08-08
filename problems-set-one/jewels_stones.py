def numJewelsInStones(J, S):
    Jset = set(J)
    return sum(s in Jset for s in S)

jewels = "aA"
stones = "aAAbbbb"
ans = numJewelsInStones(jewels,stones)
print (ans)