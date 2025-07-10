import re
import string
import random
def load_passwords(path):
    with open(path,'r') as file:
        return set(line.strip().lower() for line in file)
def check_passwords(password,common_passwords):
    if password.lower() in common_passwords:
        print("This password is too common and easily guessable!")
        return True
    else:
        print("Good choice! This password isn't commonly used.")
        return False
def generate_password(length=16):
    chars=string.ascii_letters+string.digits+string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))
def strength(password):
    score=0
    if len(password)>=8:
        score+=1
    if re.search(r"[A-Z]",password):
        score+=1
    if re.search(r"[a-z]",password):
        score+=1
    if re.search(r"[0-9]",password):
        score+=1
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        score+=1
    return score
path=r"D:\passwords.txt"
password=input("Enter a password to check:").strip()
common_passwords=load_passwords(path)
is_common=check_passwords(password,common_passwords)
score=strength(password)
print(f"Strength:{score}/5")
if score<= 2 or is_common:
    print("Your password is too weak.")
    print("Try this stronger one:",generate_password())
elif 3<=score<=4:
    print("Your password is moderate — not bad, but it could be stronger.")
    print("Here's a better one to consider:",generate_password())
else:
    print("Great! Your password is strong and secure.")


