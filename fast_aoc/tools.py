""" Module with tools that can be used for solving
"""
import collections


def parse_input(typ=None, sep=' '):
    """
    :param typ: Type of resulting input. By default it will try to parse every item in either int or float.
        If that won't work it will leave it in string form
    :type typ: type
    :param sep: A string separator between multiple entries in a single line
    :type sep: str
    """
    is_function = isinstance(typ, collections.Callable)
    real_input_type = None if is_function else typ

    def parse_decorator(solution):

        def parsing_solution(raw_input):

            parsed_input = [parse_line(line, typ=real_input_type, sep=sep)
                            for line in raw_input.strip('\n').split('\n')]

            if len(parsed_input) == 1:
                parsed_input = parsed_input[0]

            return solution(parsed_input)

        return parsing_solution

    if is_function:
        return parse_decorator(typ)

    return parse_decorator


def parse_line(line, typ=None, sep=' '):
    """ Parse a single line
    """
    parsed_line = [parse_item(item, typ=typ) for item in line.strip().strip(sep).split(sep)]

    if len(parsed_line) == 1:
        return parsed_line[0]

    return parsed_line


def parse_item(item, typ=None):
    """ Parse a single item
    """
    type_candidates = [int, float] if typ is None else [typ]

    for type_candidate in type_candidates:
        try:
            return type_candidate(item)
        except ValueError:
            pass

    return item
