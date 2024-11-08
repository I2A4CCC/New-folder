# Write code below 💖

#creating a slot machine.py
# importing module
import random

def play():
  symbols = ['🍒',' 🍇', '🍉', '7️⃣']
  result = random.choices(symbols, k=3)
  print(result)
  while result[0] != symbols[3] or result[1] != symbols[3] or result[2] != symbols[3]:
    symbols = ['🍒',' 🍇', '🍉', '7️⃣']
    result = random.choices(symbols, k=3)
    new_attempt = str(input('press enter to try again : '))
    if new_attempt == str('y') or str('n'):
      print(result) 
    else:
      print('Thanks for trying')

  if result[0] == symbols[3] and result[1] == symbols[3] and result[2] == symbols[3]:
    print("Jackpot! 💰")
play()