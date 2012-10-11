
import data_generators as gen
from user_interface import *
import random

def type_of_literal():
    literal_gens = {
        str: gen.any_str,
        int: gen.any_int,
        float: gen.any_float,
        list: gen.any_list,
        dict: gen.any_dict
    }

    literal_type, literal_gen = random.choice(literal_gens.items())
    literal = literal_gen()

    def question():
        show_text("Select the type of this value: %r" % literal)
        choices = [(type_obj.__name__, type_obj) for type_obj in literal_gens]
        choices.sort(key=lambda choice: choice[0])
        answer = multiple_choice(choices)
        return answer == literal_type
    return question

templates = (type_of_literal,)
