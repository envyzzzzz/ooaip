import random
import math

def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = str(math.gcd(num1, num2))
    question = f"{num1} {num2}"
    return question, correct_answer

def main():
    from VD_games.engine import run_game
    description = "Find the greatest common divisor of given numbers."
    run_game(generate_question, description)

if __name__ == "__main__":
    main()
