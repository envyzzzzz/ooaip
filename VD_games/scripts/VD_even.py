import random

def is_even(number):
    return number % 2 == 0

def generate_question():
    number = random.randint(1, 100)
    correct_answer = "yes" if is_even(number) else "no"
    return str(number), correct_answer

def main():
    from VD_games.engine import run_game
    run_game(generate_question, 'Answer "yes" if the number is even, otherwise answer "no".')

if __name__ == "__main__":
    main()
