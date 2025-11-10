from .cli import welcome_user

def run_game(get_question_and_answer, description):
    print("Welcome to the VD Games!")
    name = welcome_user()
    print(description)
    
    rounds_count = 3
    correct_answers = 0
    
    while correct_answers < rounds_count:
        question, correct_answer = get_question_and_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip().lower()
        
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
            
    print(f"Congratulations, {name}!")
