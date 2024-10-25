# Write code below 💖

#creating a slot machine.py
# importing module
import random

def play():
  symbols = ['🍒',' 🍇', '🍉', '7️⃣']
  result = random.choices(symbols, k=3)
  print(result)
  while result[0] != symbols[3] or result[1] != symbols[3] or result[2] != symbols[3]:
    if result[0] == symbols[3] and result[1] == symbols[3] and result[2] == symbols[3]:
       print( "Jackpot! 💰")
    else:
       new_attempt = input('press y or n try again or press x to exit : ')
       if new_attempt == 'y' or 'n':
          print(result) 
       elif new_attempt == 'x':
          print('Thanks for trying') 
       else:
          break
       
play()