#!/usr/bin/env python2

import random

class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __str__(self):
        return self.text

def read_questions(file_path):
    questions = []
    with open(file_path) as f:
        question = read_question(f)
        while question is not None:
            questions.append(question)
            question = read_question(f)
    return questions

def read_question(file_handle):
    question_text = file_handle.readline().strip()
    question_answer = file_handle.readline().strip()

    # Ignore separator line
    file_handle.readline()

    if question_text == '' or question_answer == '':
        return None

    return Question(question_text, question_answer)

def evaluate_answer(question, answer):
    return question.answer == answer

def ask(question):
    while True:
        print
        print question
        answer = raw_input(">>> ")
        answered_correctly = evaluate_answer(question, answer)
        if answered_correctly:
            print "*** CORRECT ***"
            break
        else:
            print "Incorrect, try again"


def main():
    questions = read_questions('questions.txt')
    random.shuffle(questions)

    for question in questions:
        ask(question)

if __name__ == '__main__':
    main()
