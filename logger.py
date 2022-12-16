from datetime import datetime as dt
path = 'log.txt'

def logger_one(first, second, oper, res):
    log = f'{dt.now()} | {first} {oper} {second} = {res}\n'
    with open(path, 'a') as data:
        data.write(log)


def logger_two(math_var, res):
    log = f'{dt.now()} | {math_var} = {res}\n'
    with open(path, 'a') as data:
        data.write(log)

# import logging
#
# def logger_two(math_var, res):
#     # logging.basicConfig(level=logging.DEBUG, filename="thecode.log")
#     logging.basicConfig(level=logging.INFO, filename="thecode.log", filemode="a", format="%(asctime)s %(levelname)s %(message)s")
#     logging.INFO(str(math_var) + '=' + int(res))
