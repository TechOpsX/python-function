def square(x):
    return x ** 2


# 不推荐将lambda赋值给参数值
lambda_square = lambda x: x ** 2


def lambda_func():
    numbers = [1, 2, 3, 4]
    # 作为参数进行传递
    print(list(filter(lambda x: x % 2, numbers)))


# lambda嵌套
action = (lambda x: (lambda y: x + y))


if __name__ == "__main__":
    print(square(3))
    print(lambda_square(3))
    lambda_func()
    print(action(3)(4))
