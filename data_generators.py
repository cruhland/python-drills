import random

def make_str_gen():
    with open('words.txt') as words_file:
        words = [word.strip() for word in words_file]

    while True:
        yield random.choice(words)

str_gen = make_str_gen()

def make_int_gen():
    while True:
        yield random.randint(-100, 100)

int_gen = make_int_gen()

def make_float_gen():
    while True:
        yield round(random.uniform(-100.0, 100.0), 2)

float_gen = make_float_gen()

simple_gens = (str_gen, int_gen, float_gen)

def make_list_gen():
    global simple_gens

    while True:
        length = random.randint(0, 7)
        yield [one_of(simple_gens).next() for index in xrange(length)]

list_gen = make_list_gen()

def make_dict_gen():
    global simple_gens

    while True:
        length = random.randint(0, 7)
        yield {one_of(simple_gens).next(): one_of(simple_gens).next()
               for index in xrange(length)}

dict_gen = make_dict_gen()

def make_filter(predicate):
    def do_filter(gen):
        while True:
            next_value = gen.next()
            if predicate(next_value):
                yield next_value
    return do_filter

def one_of(gens):
    return random.choice(gens)
