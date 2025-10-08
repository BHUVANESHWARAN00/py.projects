password = input("Enter your password: ")

length = len(password)
has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    else:
        has_special = True  
score = 0

if length >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_special:
    score += 1

if score == 5:
    strength = "Very Strong"
elif score == 4:
    strength = "Strong"
elif score == 3:
    strength = "Medium"
elif score == 2:
    strength = "Weak"
else:
    strength = "Very Weak"

print(f"Your password is {strength}")
