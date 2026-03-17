import random
import time

quotes = [
    "Success is not final, failure is not fatal.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "First, solve the problem. Then, write the code.",
    "Programs must be written for people to read.",
    "Simplicity is the soul of efficiency."
]

print("🚀 Python Docker App Started...\n")

for i in range(5):
    print(f"Quote {i+1}: {random.choice(quotes)}")
    time.sleep(1)

print("\n✅ App Finished")
