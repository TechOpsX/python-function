"""
位置参数、默认参数、可变参数、关键字参数、命名参数
位置参数 > 默认参数 > 可变参数（或*）> 命名关键字参数 > 关键字参数（当存在命名关键字参数时无效）
"""


def named_keywords_params_func(name, age, *, qq):
    """
    如果要限制只能传指定名字的参数，则可以使用命名关键字参数
    命名关键字参数，是对关键字参数方式的进一步约束，更安全了
    定义需要一个*号作为分隔符，*后面的参数表示只能传递该名字的参数
    如下表示两个位置参数，还有一个名为qq的关键字参数，调用时传其它名字会报错
    """
    print(name, age, qq)


def named_keywords_params_func2(name, age, *info, qq, **kwargs):
    """
    #如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
    """
    print(name, age, *info, qq, kwargs)


if __name__ == "__main__":
    # 必须传入参数qq，否则会报错
    # named_keywords_params_func("Lily", 18)
    named_keywords_params_func("Lily", 18, qq="1028988")
    # 必须传入参数qq，否则会报错
    # named_keywords_params_func2("Lily", 18, sex="female")
    named_keywords_params_func("Lily", 18, qq="10289881")
