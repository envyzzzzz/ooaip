import random

def generate_progression():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    
    progression = []
    for i in range(length):
        progression.append(str(start + i * step))
    
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    
    question = " ".join(progression)
    return question, correct_answer

def main():
    from VD_games.engine import run_game
    run_game(generate_progression, "What number is missing in the progression?")

if __name__ == "__main__":
    main()
