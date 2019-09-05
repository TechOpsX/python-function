def variable_params_func(*args):
    """
    args是一个tuple
    参数中的*args 可以理解为将,隔开的变量转换为列表，并用args指向列表
    """
    # *args解包列表，获取列表中的数值
    print(*args)
    print(type(args))


if __name__ == '__main__':
    variable_params_func('a')
    variable_params_func('a', 'b', 'c')
