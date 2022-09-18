n=int(input())
sum=0
while n:
   r=n%10
   sum+=r
   n=n//10
   if n==0:
      if  sum<=9:
          print(sum)
      else:
           n=sum
           sum=0