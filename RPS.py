import random
print("..........ROCKS..........")
print("..........PAPERS..........")
print("........SCISSORS........")
p1 = input("enter your choice:  ")
comp = random.randint(0,2)
if comp == 0:
     comp = 'rocks'
elif comp == 1:
     comp = 'paper'
else:
     comp = 'scissors'
print("your choice: " +p1)
print("computer's choice: "+comp)
if p1:
     if p1 == comp:
          print("IT'S A TIE")
     if p1=='rocks':
          if comp=='scissors':
               print("P1 WINS")
          elif comp=='paper':
               print("comp WINS")
     elif p1=='paper':
          if comp=='rocks':
               print("P1 WINS")
          elif comp=='scissors':
               print("comp WINS")
     elif p1=='scissors':
          if comp=='paper':
               print("P1 WINS")
          elif comp=='rocks':
               print("comp WINS")
     else:
          print("ENTER A VALID CHOICE")
else:
      print("ENETR A CHOICE")   
     
