import prompt


def greeting():
    print('Welcome to the Brain Games!')


def get_user_name():
    return prompt.string('May I have your name? ')


def get_user_answer():
    return prompt.string('Your answer: ')


def cli():
    greeting()
    name = get_user_name()
    print(f'Hello, {name}!')
