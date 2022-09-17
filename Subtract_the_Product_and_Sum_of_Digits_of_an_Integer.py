n=int(input())
product=1
sum=0
while n:
    r=n%10
    product*=r
    sum+=r
    n=n//10
print(product-sum)
