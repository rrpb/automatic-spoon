def subtract_product_and_sum(n):
    prod=1
    sum=0
    while n!=0:
        digit = n%10
        sum += digit
        prod*=digit
        n=n//10
    return prod-sum

print (subtract_product_and_sum(435))