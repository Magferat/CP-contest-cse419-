t = int(input().strip())


while t > 0:

   n, k = [int(i) for i in input().split()]
   if n % 2 == 0 :
       print('yes')

   else:
       if k % 2 == 0:
           print('no')
       else:
           print('yes')

   t -= 1