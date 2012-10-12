
import data_generators as gen
from user_interface import *
import random
import ast

def type_of_literal():
    literal_gens = {
        str: gen.str_gen,
        int: gen.int_gen,
        float: gen.float_gen,
        list: gen.list_gen,
        dict: gen.dict_gen
    }

    literal_type, literal_gen = random.choice(literal_gens.items())
    literal = literal_gen.next()

    def question():
        show_text("Select the type of this value: %r" % literal)
        choices = [(type_obj.__name__, type_obj) for type_obj in literal_gens]
        choices.sort(key=lambda choice: choice[0])
        answer = multiple_choice(choices)
        return answer == literal_type
    return question

def list_subscripting():
    a_list = gen.make_filter(lambda seq: len(seq) > 0)(gen.list_gen).next()
    index = random.randrange(len(a_list))
    message = "Let some_list = %r. " + \
              "Select the element at index %d in some_list."
    def question():
        show_text(message % (a_list, index))
        answer = raw_input(">>> ")
        parsed_answer = ast.parse(answer)
        list_name_correct = parsed_answer.body[0].value.value.id == 'some_list'
        list_index_correct = parsed_answer.body[0].value.slice.value.n == index
        return list_name_correct and list_index_correct
    return question

templates = (type_of_literal, list_subscripting)
