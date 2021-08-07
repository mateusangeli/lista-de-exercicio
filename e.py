for num in range (0,16):
  if (num == 0):
    print("3^", num, "=", 1)
  elif(num==1):
    print("3^", num, "=", 3)
  else:
    cont = 0
    r = 1
    while(cont < num):
      r *=3
      cont +=1
    print("3^", num, "=", r)