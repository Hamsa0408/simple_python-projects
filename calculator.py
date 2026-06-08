 return display
def calfunction(choice):
  if choice == 1:
    print("performing addition")
    a,b=user_input()
    return a+b
  elif choice == 2:
    print("performing subtraction")
    a,b=user_input()
    return a-b
  elif choice == 3:
    print("performing division")
    a,b=user_input()
    return a/b
  elif choice == 4:
    print("performing multiplication")
    a,b=user_input()
    return a*b
  else:
    print("invalid input")
def user_input():
  print("enter two values")
  n=int(input("enter first number"))
  n2=int(input("enter second number"))
  return n,n2
def main():
  caldisplay()
  while True:
    val=int(input("enter choice:"))
    return calfunction(val)
main()