# Write a Python program that takes a numeric grade from the user (between 0 and 100), and prints the corresponding letter grade:
# 90–100 → A
# 80–89  → B
# 70–79  → C
# 60–69  → D
# <60    → F
# Your program should handle the following exceptions:
#
# If the user enters a non-numeric value, catch the ValueError and display a user-friendly message.
# If the user enters a number outside the valid range (0 to 100), raise a ValueError yourself with a custom message.
# Use the try–except–else–finally structure:
#
# try: Attempt to parse the input and compute the letter grade.
# except: Handle conversion errors and invalid ranges.
# else: Print the final grade if everything was successful.
# finally: Print a goodbye message like "Thank you for using the Grade Calculator. Goodbye!" no matter what.



def calculate_letter_grade(score: int) -> str:
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"

try:
    user_input = input("Enter your grade (0–100): ")
    grade = int(user_input)

    if grade < 0 or grade > 100:
        raise ValueError("Grade must be between 0 and 100.")

    letter = calculate_letter_grade(grade)
except ValueError as ve:
    print(f"{ve}")
else:
    print(f"Your letter grade is: {letter}")
finally:
    print("Thank you for using the Grade Calculator. Goodbye!")


