import random
import operator

def calculate_expression(num1, num2, operation):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    return operations[operation](num1, num2)

def main():
    from VD_games.cli import welcome_user
    
    print("Welcome to the VD Games!")
    name = welcome_user()
    print("What is the result of the expression?")
    
    correct_answers_needed = 3
    correct_answers_count = 0
    
    while correct_answers_count < correct_answers_needed:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        operation = random.choice(['+', '-', '*'])
        
        correct_answer = str(calculate_expression(num1, num2, operation))
        question = f"{num1} {operation} {num2}"
        
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
