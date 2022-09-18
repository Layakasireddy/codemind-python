N=int(input())
sqr=N*N
rev=0
rev_2=0
while N>0:
     digit=N%10
     rev=rev*10+digit
     N=N//10
     sqr_rev=rev*rev
while sqr_rev>0:
   digit_2=sqr_rev%10
   rev_2=rev_2*10+digit_2
   sqr_rev=sqr_rev//10
if sqr==rev_2:
    print("True")
else:
     print("False")