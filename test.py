import random

# List of your 20 questions
questions = [
    "tell me about your self",
    "What is python",
    "Tell me about your project",
    "list vs tuple",
    "why python is general purpose programming language??",
    "why python is Dynamically typed programming language??",
    "'is' operator  vs '==' operator",
    "python is complied or interpreted programming language",
    "PVM",
    "How python works",
    "what is bytecode",
    "how is memory managed  in py",
    "what is garbage collector in py",
    "what is list comprehension",
    "what is ternary/conditional operator",
    "memory allocation in py",
    "can we run python 3 code on python 2 interpreter",
    "what is pep8",
]


# Function to get a random question and remove it from the list
def get_random_question():
    if questions:
        random_question = random.choice(questions)
        questions.remove(random_question)
        return random_question
    else:
        return "No more questions left."


# Main program
while True:
    print("Press Enter to get a random question or 'q' to quit...")
    user_input = input()

    if user_input.lower() == 'q':
        break

    random_question = get_random_question()
    print(random_question)

print("Program ended.")
