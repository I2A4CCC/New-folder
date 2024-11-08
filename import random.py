import random
i = 200
while i > 100:
 symbols = ['🍒',' 🍇', '🍉', '7️⃣']
 result = random.choices(symbols, k=3)
 i -= 1
 print(result)
