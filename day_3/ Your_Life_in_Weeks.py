# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
life_left=(90-int(age))

weeks=(life_left*52)

months=(life_left*12)

days=(life_left*365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")