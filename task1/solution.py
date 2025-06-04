def strict(func):
    def wrapper(*args):
        func_args_with_type = func.__annotations__

        if 'return' in func_args_with_type.keys():
            del func_args_with_type['return']

        if len(args) != len(func_args_with_type):
            raise IndexError(
                'Количество переданных переменных в функцию не совпадает с '
                'количеством объявленных переменных функции.')

        for i, (arg_name, arg_type) in enumerate(func_args_with_type.items()):
            if type(args[i]) is not arg_type:
                raise TypeError(
                    'Тип переданной переменной не совпадает с типом переменной'
                    f', объявленным в функции:\nДля переменной "{arg_name}" '
                    f'объявлен тип - {arg_type}, а передан - {type(args[i])}')

        return func(*args)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b
