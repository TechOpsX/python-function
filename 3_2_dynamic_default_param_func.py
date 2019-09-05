import time


def dynamic_default_param_func(log_time=time.time()):
    # 默认参数在函数定义加载的时候，就已经确定了
    # 推荐使用None和doc的方式来使用动态默认参数
    print(log_time)


if __name__ == '__main__':
    dynamic_default_param_func()
    time.sleep(2)
    dynamic_default_param_func()
