def no_return_func():
    a = 1


def return_one_value():
    return 1


def return_two_value():
    return 1, 2


if __name__ == "__main__":
    print(no_return_func())
    print(return_one_value())
    print(return_two_value())
    a, b = return_two_value()
    print(a, b)

    # 只接受一个值，可以用_作为占位符，放弃接收值
    _, c = return_two_value()
    print(c)
