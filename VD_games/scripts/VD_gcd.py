import random
import math

def main():
    from ..cli import welcome_user
    
    print("Welcome to the VD Games!")
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    
    correct_answers_needed = 3
    correct_answers_count = 0
    
    while correct_answers_count < correct_answers_needed:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        
        correct_answer = str(math.gcd(num1, num2))
        question = f"{num1} {num2}"
        
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()
        
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
            
    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()
