numbers = [ 3, 7, 2, 15, 9, 20, 5, 14, 12, 1, 8, 11, 6, 19, 4, 10, 17, 13, 16, 18]
even=[]
odd=[]
for i in numbers:
    if(i%2==0):
      even.append(i)  
    else:
       odd.append(i)
print(f"Even Numbers are:{even}")
print(f"Odd Numbers are:{odd}")