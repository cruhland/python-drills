#!/usr/bin/env python2

import random
import question_templates

def main():
    while True:
        template = random.choice(question_templates.templates)
        question = template()
        while True:
            print
            answered_correctly = question()
            if answered_correctly:
                print "*** CORRECT ***"
                break
            else:
                print "Incorrect, try again"

if __name__ == '__main__':
    main()
