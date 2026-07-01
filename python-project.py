"""
Project 1 - Smart Student Wellness Analyzer

Author: Krish Chhabra

Description:
This is my first Python project built after learning
Python Basics, Data Types, Operators, Strings,
If-Else Statements and Loops.

BASED ON MY Day1 - Day3 Learning
"""

print("=" * 50)
print("     SMART STUDENT WELLNESS ANALYZER")
print("=" * 50)

# ----------------------------
# Student Details
# ----------------------------

while True:
    name = input("Enter your name: ").strip()

    if name == "":
        print("Name cannot be empty.")
    else:
        break

while True:
    age = int(input("Enter your age: "))

    if age < 1 or age > 100:
        print("Please enter a valid age.")
    else:
        break

while True:
    hours_studied = float(input("Hours studied today: "))

    if hours_studied < 0:
        print("Hours cannot be negative.")
    else:
        break

while True:
    hours_slept = float(input("Hours slept today: "))

    if hours_slept < 0:
        print("Hours cannot be negative.")
    else:
        break

while True:
    water_intake = float(input("Water intake (Litres): "))

    if water_intake < 0:
        print("Please enter a valid value.")
    else:
        break

while True:
    screen_time = float(input("Screen time (Hours): "))

    if screen_time < 0:
        print("Please enter a valid value.")
    else:
        break

while True:
    exercise_minutes = float(input("Exercise (Minutes): "))

    if exercise_minutes < 0:
        print("Please enter a valid value.")
    else:
        break

print("\n")
print("=" * 50)
print("          SMART STUDENT REPORT")
print("=" * 50)

print(f"Student Name      : {name}")
print(f"Age               : {age}")
print(f"Study Hours       : {hours_studied}")
print(f"Sleep Hours       : {hours_slept}")
print(f"Water Intake      : {water_intake} L")
print(f"Screen Time       : {screen_time} Hours")
print(f"Exercise          : {exercise_minutes} Minutes")

print("\n")
print("-" * 50)
print("STUDY RATING")
print("-" * 50)

if hours_studied <= 1:
    print("Poor - Try to study at least 2-3 hours daily.")
elif hours_studied <= 2:
    print("Average - You can improve your consistency.")
elif hours_studied <= 4:
    print("Good - Keep working hard.")
else:
    print("Excellent - Great dedication!")

print("\n")
print("-" * 50)
print("SLEEP RATING")
print("-" * 50)

if hours_slept <= 3:
    print("Very Poor - You need more sleep.")
elif hours_slept <= 5:
    print("Below Average - Try sleeping 6-7 hours.")
elif hours_slept <= 8:
    print("Excellent - Healthy sleep schedule.")
else:
    print("Too Much Sleep - Maintain a balanced routine.")

print("\n")
print("-" * 50)
print("WATER INTAKE")
print("-" * 50)

if water_intake < 2:
    print("Poor - Drink more water.")
elif water_intake < 3:
    print("Good - Stay hydrated.")
elif water_intake <= 4:
    print("Excellent - Keep it up.")
else:
    print("Very High - Avoid overhydration.")

print("\n")
print("-" * 50)
print("SCREEN TIME")
print("-" * 50)

if screen_time >= 6:
    print("Very High - Reduce screen time.")
elif screen_time >= 4:
    print("High - Try to limit unnecessary usage.")
elif screen_time >= 2:
    print("Good - Balanced screen time.")
else:
    print("Excellent - Healthy digital habits.")

print("\n")
print("-" * 50)
print("EXERCISE")
print("-" * 50)

if exercise_minutes < 20:
    print("Low - Exercise a little more.")
elif exercise_minutes < 45:
    print("Good - Nice effort.")
else:
    print("Excellent - Great job staying active.")

print("\n")
print("=" * 50)
print("PERSONALIZED SUGGESTIONS")
print("=" * 50)

if hours_studied < 2:
    print(" Increase your daily study hours.")

if hours_slept < 6:
    print(" Sleep at least 6-7 hours.")

if water_intake < 3:
    print("Drink more water to stay hydrated.")

if screen_time > 4:
    print(" Reduce unnecessary screen time.")

if exercise_minutes < 30:
    print(" Try exercising for at least 30 minutes daily.")

print("\nKeep learning and stay healthy!")
print("=" * 50)