def make_question():
    number = generate_number()
    question = f'Question: {number}'
    answer = correct_answer(number)
    return (question, answer)

def generate_number():
    
    return randint(1, 100)

def correct_answer(number):
    
    return 'no' if number % 2 else 'yes'

def check_answer(user_answer, correct_answer):
    
    if user_answer == correct_answer:
        message = 'Correct!'
        return (True, message)
    message = "'{wrong}' is wrong answer ;(. Correct answer was '{correct}'."
    return (False, message.format(wrong=user_answer, correct=correct_answer))