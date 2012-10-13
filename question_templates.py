
import data_generators as gen
from user_interface import *
import random
import ast

literal_gens = {
    str: gen.str_gen,
    int: gen.int_gen,
    float: gen.float_gen,
    list: gen.list_gen,
    dict: gen.dict_gen
}

def type_of_literal():
    global literal_gens
    literal_type, literal_gen = random.choice(literal_gens.items())
    literal = literal_gen.next()

    def question():
        show_text("Select the type of this value: %r" % literal)
        choices = [(type_obj.__name__, type_obj) for type_obj in literal_gens]
        choices.sort(key=lambda choice: choice[0])
        answer = multiple_choice(choices)
        return answer == literal_type
    return question

def literal_of_type():
    """Pick the literal of the given type from a list of options."""
    global literal_gens
    random_type = random.choice(literal_gens.keys())

    def question():
        text = "Select the value of type {0}:".format(random_type.__name__)
        show_text(text)
        choices = [(repr(type_gen.next()), type_obj)
                   for type_obj, type_gen in literal_gens.iteritems()]
        random.shuffle(choices)
        answer = multiple_choice(choices)
        return answer == random_type
    return question

def list_subscripting():
    list_var = gen.str_gen.next()
    element_name, seq_gen = \
        random.choice([("element", gen.list_gen), ("character", gen.str_gen)])
    a_list = gen.make_filter(lambda seq: len(seq) > 0)(seq_gen).next()
    index = random.randrange(len(a_list))
    position_func = random.choice([index_position, ordinal_position])
    position = position_func(index, element_name)
    message = "Let {var} = {value!r}. Select the {position} in {var}."

    def question():
        text = message.format(var=list_var, value=a_list, position=position)
        show_text(text)
        answer = raw_input(">>> ")
        parsed_answer = ast.parse(answer)
        list_name_correct = parsed_answer.body[0].value.value.id == list_var
        list_index_correct = parsed_answer.body[0].value.slice.value.n == index
        return list_name_correct and list_index_correct
    return question

def index_position(index, element_name):
    text = "{element} at index {index}"
    return text.format(element=element_name, index=index)

def ordinal_position(index, element_name):
    n = index + 1
    return "{n}{suffix} {element}".format(
        n=n,
        suffix=ordinal_suffix(n),
        element=element_name
    )

def ordinal_suffix(n):
    if 11 <= n % 100 <= 13:
        return "th"
    else:
        return {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")

templates = (type_of_literal, literal_of_type, list_subscripting)
