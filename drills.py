#!/usr/bin/env python2

import random
from sys import argv
from question_templates import templates

def main():
    print
    print "Python drills"
    print "At any time, press ^D to skip a question, or ^C to quit."

    if len(argv) > 1:
        question_selection = [templates[name] for name in argv[1:]]
    else:
        question_selection = templates.values()

    while True:
        template = random.choice(question_selection)
        question = template()
        while True:
            print
            try:
                answered_correctly = question()
                if answered_correctly:
                    print "*** CORRECT ***"
                    break
                else:
                    print "Incorrect, try again"
            except EOFError:
                print "\nSkipping..."
                break
            except KeyboardInterrupt:
                print "\nQuitting..."
                return

if __name__ == '__main__':
    main()
