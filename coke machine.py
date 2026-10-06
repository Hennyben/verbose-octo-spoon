def coke():
     x=50

     while x >= 0:
          print(f"Amount due: {x}")
          y=int(input("Coin: "))
          if y == 5 or y ==10 or y== 25:
               x-=y
          

     if x < 0:
          f=x*-1
          print(f"changed owed:{f}")
coke()



