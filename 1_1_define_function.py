"""
本节讨论的是如何定义一个函数与调用函数？
使用 def 开始函数定义，紧接着是函数名，括号内部为函数的参数，内部为函数的 具体功能实现代码，如果想要函数有返回值, 在 expressions 中的逻辑代码中用 return 返回。
函数命名规则：函数名应该小写，如果想提高可读性可以用下划线分隔。
"""


def my_factorial(num):
    """
    Solve factorial

    :param num: Non-negative integer
    :return: number's factorial
    """
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


if __name__ == '__main__':
    # 调用自定义函数
    print(my_factorial(3))
    # 打印当前模块的全部属性，定义的函数添加到属性中，属性key为函数的名字
    print(globals())
