import model
import view
import logger
import logging

def start():
    my_calc = view.choice_calc()
    if my_calc == 2:
        model.set_first_number(view.input_number())
        math_var = model.get_first_number()
        model.eval_str()
        res = model.get_intermediate_result()
        logger.logger_two(math_var, res)
    else:
        model.set_first_number(view.input_number())
        model.get_first_number()
        operation = view.input_operation()
        while operation != '=':
            # first = model.get_intermediate_result()
            first = model.get_first_number()
            model.set_next_number(view.input_number())
            second = model.get_next_number()
            oper = operation
            model.check_operation(operation)
            res = model.get_intermediate_result()
            view.print_result(model.get_intermediate_result())
            logger.logger_one(first, second, oper, res)
            operation = view.input_operation()

    view.print_result(model.get_intermediate_result())

