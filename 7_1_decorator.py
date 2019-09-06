import functools


def log(func):
    # 将wrapper函数的__name__属性动态替换为func的__name__
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


# 等价于now = log(now), 此时为wrapper函数
@log
def now():
    print('2015-3-25')


# 首先执行log2('execute')函数， 返回decorator函数
@log2('execute')
def now2():
    print('2015-3-25')


@log2('execute')
@log
def now3():
    print('2015-3-25')


if __name__ == "__main__":
    now()
    print(now.__name__)
    # 装饰器嵌套
    now3()
