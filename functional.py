import numpy as np


def sequential_map(*args):
    result = func_chain(*args[:-1])(args[-1])
    if type(result[0]) == float or type(result[0]) == np.float64:
        return list(map(int, result))
    else:
        return result


def consensus_filter(*args):
    container = args[-1]
    for func in args[:-1]:
        container = list(filter(func, container))
    return container


def conditional_reduce(func1, func2, container):
    container = list(filter(func1, container))
    if len(container) < 2:
        print('Not enough arguments to perform', func2.__name__)
    elif len(container) > 2:
        print('Too many arguments', func2.__name__, 'takes only 2 arguments')
    else:
        return func2(container[0], container[1])


def func_chain(*args):
    def resulting_func(container):
        for func in args:
            container = func(container)
        return container

    return lambda x: resulting_func(x)


def multiple_partial(*args, **kwargs):  # ???
    result = []
    for func in args:
        def partial(func, *args, **kwargs):
            def newfunc(*fargs, **fkwargs):
                newkwargs = {**kwargs, **fkwargs}
                return func(*args, *fargs, **newkwargs)

            newfunc.func = func
            newfunc.args = args
            newfunc.kwargs = kwargs
            return newfunc

        result.append(partial(func, *args, **kwargs))
    return result
