import os
import random

os.system('clear')
print("=========================================")
print("         NUMBER GUESSING GAME            ")
print("=========================================")
print("created by - priyamshu hacker ")
print("[+] Maine 1 se 50 ke beech ek number socha hai.")
print("[+] Kya aap guess kar sakte hain?\n")

secret_number = random.randint(1, 50)
attempts = 0

while True:
    try:
        guess = int(input("👉 Aapka andaza (Guess): "))
        attempts += 1
        
        if guess < secret_number:
            print("[🔼] Thoda BADA number sochiye!\n")
        elif guess > secret_number:
            print("[🔽] Thoda CHOTA number sochiye!\n")
        else:
            print(f"\n[🎉] Wah bhai wah! Sahi andaza lagaya!")
            print(f"[🏆] Aapne kul {attempts} baar me jeet hasil ki!")
            print("=========================================")
            break
            
    except ValueError:
        print("[!] Kripya ek valid number type kare!\n")
