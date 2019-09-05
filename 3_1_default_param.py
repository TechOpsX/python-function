def default_param_func(a, b=1):
    """
    默认参数必须在参数后面，如default_param_func(a=1, b)是错误的
    """
    return a + b


if __name__ == '__main__':
    print(default_param_func(1))
    print(default_param_func(1, 2))
