n=int(input("ENTER A NUMBER:"))
fact=1
count=2
if n==0:
  print("FACTORIAL OF 0 IS 1")
if n>0:
  while(count<=n):
    fact=fact*count
    count=count+1
    print("THE FACTORIAL OF GIVEN NUMBER",fact)