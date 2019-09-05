def foo():
    """
    指明变量a来源于全局变量
    """
    global a
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 200
