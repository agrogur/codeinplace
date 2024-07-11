import random

def main():
    print("Khansole Academy")
    import random

def generate_problem():
    """Generates a simple addition problem with two 2-digit integers."""
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    return num1, num2

def get_user_answer():
    """Reads the user's answer from input."""
    try:
        answer = int(input("Your answer: "))
        return answer
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_user_answer()

def check_answer(num1, num2, answer):
    """Checks if the user's answer is correct."""
    expected_answer = num1 + num2
    if answer == expected_answer:
        print("Correct!")
        return True
    else:
        print("Incorrect. The expected answer is", expected_answer)
        return False

def khansole_academy():
    """Main function to run the Khansole Academy program."""
    print("Khansole Academy")

    correct_count = 0
    while correct_count < 3:
        num1, num2 = generate_problem()
        print("What is", num1, "+", num2, "?")
        answer = get_user_answer()
        if check_answer(num1, num2, answer):
            correct_count += 1
            print("You've gotten", correct_count, "correct in a row.")
        else:
            correct_count = 0

    print("Congratulations! You mastered addition.")

# Run the Khansole Academy program
khansole_academy()

    
    
if __name__ == '__main__':
    main()