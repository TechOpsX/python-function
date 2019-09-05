def foo():
    b = 'hello'

    def bar():  # Python中可以在函数内部再定义函数
        # 指明变量b来源于嵌套变量
        # nonlocal b
        b = "world"
        print(b)

    bar()
    print(b)


if __name__ == '__main__':
    foo()
