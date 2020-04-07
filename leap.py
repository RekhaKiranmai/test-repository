n=int(input())
if n%4==0:
   if n%100==0:
      if n%400==0:
         print("leap")
      else:
         print("not leap")
   else:
      print("leap")
         
else:
   print("non-leap")
print("changes to test")
