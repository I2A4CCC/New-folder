# Write code below 💖

#creating a slot machine.py
# importing module
import random

symbols = ['🍒',' 🍇', '🍉', '7️⃣']

def play():
  result = random.choices(symbols, k=3)

  print(result)
  while result[0] != '7️⃣' or result[1] != '7️⃣' or result[2] != '7️⃣':
    symbols = ['🍒',' 🍇', '🍉', '7️⃣']
    result = random.choices(symbols, k=3)
    new_attempt = str(input('press enter to try again : '))
    if new_attempt == str('y') or str('n'):
      print(result) 
    else:
      print('Thanks for trying')

  if result[0] == '7️⃣' and result[1] == '7️⃣' and result[2] == '7️⃣':
    print("Jackpot! 💰")
    

play()