print("1.cel to f /n2.f to cel")
opt=int(input("enter option in 1 or 2"))
if opt == 1:
  cel=int(input("enter the temp in cel"))
  f=(cel*9/5)+32
  print(f)
elif opt == 2:
  print("convert feom f to cel")
  f=int(input("enter temp in f"))
  cel=(f-32)*5/9
  print(cel)
