#!/usr/bin/env python3
# -*- coding: utf-8 -*-



from brain_games.engine import run
from brain_games.games import brain_prime


def main():

    run(brain_prime)


if __name__ == '__main__':
    main()


def make_question():
    
    number = generate_number()
    question = f'Question: {number}'
    answer = 'yes' if is_prime(number) else 'no'
    return (question, answer)