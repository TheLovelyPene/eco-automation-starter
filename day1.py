# Week 1 Day 1 Exercises

# 1. Basic Variable
# Create a variable steps_today = 3000 and print it.
steps_today = 3000
print(steps_today)


# 2. If Condition
# If steps_today > 5000 → print "Goal met!", else → "Keep walking!"
if steps_today > 5000: 
    print ("Goal met!")
else: 
    print ("Keep walking!")

# 3. For Loop with a List
# daily_expenses = [5, 10, 7] → print each expense in the list.
daily_expenses = [5, 10, 7]
for expense in daily_expenses:
    print ("Expense", expense)

# 4. Real-World Example
# balance = 100 → subtract each daily_expense → print "Final balance: X".
balance = 100 
for expense in daily_expenses:
    balance -= expense
print("Final balance:", balance) 
# 5. Challenge
# Loop: keep adding 10 until balance >= 200 → print balance at each step.
while balance < 200:
    balance += 10
    print("Balance is now", balance)