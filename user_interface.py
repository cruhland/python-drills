
def show_text(text):
    print text

def multiple_choice(choices):
    for num, choice in enumerate(choices, start=1):
        show_text("%d. %s" % (num, choice[0]))

    selection = raw_input("Select an option (1-%d): " % len(choices))
    return choices[int(selection) - 1][1]
