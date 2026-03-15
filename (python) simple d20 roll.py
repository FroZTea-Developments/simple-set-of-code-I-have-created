import random
import time

print("You throw the d20 die...")
result = random.randint(1, 20)
time.sleep(1)
print("...it comes to a Stop.")
time.sleep(1)
print(f"You rolled a {result}")