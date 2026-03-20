#Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
'''*
   **
   ***'''

def print_pattern(n):
    for i in range(n+1):
        for j in range(i):
            print("*", end=" ")
        print()

print_pattern(3)