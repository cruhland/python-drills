#!/usr/bin/env python2

import random
import question_templates

def main():
    print
    print "Python drills"
    print "At any time, press ^D to skip a question, or ^C to quit."

    while True:
        template = random.choice(question_templates.templates)
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
