def keyword_param_func(name, age, **kwargs):
    """
    关键字参数必须在位置参数之后
    **kwargs接收key-value形式的参数，存入dict中
    """
    # 使用**kwargs提取qq="123"，可以用于传递到子函数中
    print(name, age, kwargs)
    print(type(kwargs))
    # 未传入使用的参数会报错，如何要求必须传入指定的参数呢？见命名关键字参数
    print(kwargs['qq'])


if __name__ == "__main__":
    keyword_param_func(18, "Lily")
    keyword_param_func(age=18, name="Lily")
    keyword_param_func(name="Helen", age=10, qq="123")
