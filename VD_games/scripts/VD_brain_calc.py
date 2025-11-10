import random
import operator

def calculate_expression(num1, num2, operation):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    return operations[operation](num1, num2)

def generate_question():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operation = random.choice(['+', '-', '*'])
    
    correct_answer = str(calculate_expression(num1, num2, operation))
    question = f"{num1} {operation} {num2}"
    return question, correct_answer

def main():
    from VD_games.engine import run_game
    run_game(generate_question, "What is the result of the expression?")

if __name__ == "__main__":
    main()
