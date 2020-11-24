ataque1 = int(input())
defesa1 = int(input())

ataque2 = int(input()) 
defesa2 = int(input()) 

ataque1 = ataque1 if not ataque1 == defesa2 else 0
ataque2 = ataque2 if not ataque2 == defesa1 else 0

if((ataque1 > 0 and ataque2 == 0) or (ataque2 > 0 and ataque1 == 0)):
  if(ataque1 > ataque2):
    print(1)
  else:
    print(2)
else:
  print(-1)
