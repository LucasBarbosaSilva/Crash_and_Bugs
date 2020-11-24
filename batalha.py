ataque1 = int(input())
defesa1 = int(input())

ataque2 = int(input()) 
defesa2 = int(input()) 

atk1 = atk1 if not atk1 == def2 else 0
atk2 = atk2 if not atk2 == def1 else 0

if((atk1 > 0 and atk2 == 0) or (atk2 > 0 and atk1 == 0)):
  if(atk1 > atk2):
    print(1)
  else:
    print(2)
else:
  print(-1)
