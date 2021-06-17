# import functools
#
#
# def my_decorator1(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('execute decorator1')
#         func(*args, **kwargs)
#
#     return wrapper
#
#
# def my_decorator2(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('execute decorator2')
#         func(*args, **kwargs)
#
#     return wrapper
#
#
# @my_decorator1
# @my_decorator2
# def greet(message):
#     print(message)
#
#
# if __name__ == '__main__':
#     greet('hello world')



# Myclass = type('Myclass', (), {"data": 1})
# instance = Myclass

# class = Myclass()
# next()

# class Mymeta(type):
#     def __init__(self, name, bases, dic):
#         super(Mymeta, self).__init__(name, bases, dic)
#         # print(Mymeta.__init__())
#
#
# def is_subsequence(a, b):
#     b = iter(b)
#     return all(i in b for i in a)

# import os
# import psutil
# import gc
# import objgraph
#
#
# # 显示当前 python 程序占用的内存大小
# def show_memory_info(hint):
#     pid = os.getpid()
#     print(pid)
#     p = psutil.Process(pid)
#
#     info = p.memory_full_info()
#     memory = info.uss / 1024. / 1024
#     print('{} memory used: {} MB'.format(hint, memory))
#
#
# def func():
#     show_memory_info('initial')
#     a = [i for i in range(10000000)]
#     show_memory_info('after a created')
#
# a = [1, 2, 3]
# b = [4, 5, 6]
#
# a.append(b)
# b.append(a)


# import unittest
#
#
# # 将要被测试的排序函数
# def sort(arr):
#     l = len(arr)
#     for i in range(0, l):
#         for j in range(i + 1, l):
#             if arr[i] >= arr[j]:
#                 tmp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = tmp
#
#
# # 编写子类继承 unittest.TestCase
# class TestSort(unittest.TestCase):
#
#     # 以 test 开头的函数将会被测试
#     def test_sort(self):
#         arr = [3, 4, 1, 5, 6]
#         sort(arr)
#         # assert 结果跟我们期待的一样
#         self.assertEqual(arr, [1, 3, 4, 5, 6])
# import pdb

# a = 1
# b = 2
# import pwd
# pdb.set_trace()
# c = 3
# print(a+b+c)
#
# def func():
#     print('enter func()')
#
#
# a = 1
# b = 2
# import pdb
#
# pdb.set_trace()
# func()
# c = 3
# print(a + b + c)




# if __name__ == '__main__':
    # unittest.main(argv=['first-arg-is-ignored'], exit=False)

    # print(objgraph.show_refs([a]))
    # func()
    # print(gc.collect())
    # show_memory_info('finished')
    # show_memory_info('ddd')
    # print(Mymeta)
    # # print(instance.data)
    # print(next(iter([1, 2])))
    # print(next(iter([1, 2])))
    # print(is_subsequence([1,3,5], [1,2,3,4,5]))
    # print(is_subsequence([1,4,3], [1,2,3,4,5]))

def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_seq(n):
    import pdb
    pdb.set_trace()
    res = []
    if n > 0:
        res.extend(fib_seq(n - 1))
        print(res)
    res.append(fib(n))
    return res


# print(fib_seq(30))

# import json
# import requests
#
# gemini_ticker = 'https://api.gemini.com/v1/pubticker/{}'
# symbol = 'btcusd'
# btc_data = requests.get(gemini_ticker.format(symbol)).json()
#
# print(json.dumps(btc_data, indent=4))

import matplotlib.pyplot as plt
import pandas as pd
import requests

# 选择要获取的数据时间段
periods = '3600'

# 通过 Http 抓取 btc 历史价格数据
resp = requests.get('https://api.cryptowat.ch/markets/gemini/btcusd/ohlc',
                    params={
                        'periods': periods
                    })
data = resp.json()

# 转换成 pandas data frame
df = pd.DataFrame(
    data['result'][periods],
    columns=[
        'CloseTime',
        'OpenPrice',
        'HighPrice',
        'LowPrice',
        'ClosePrice',
        'Volume',
        'NA'])

# 输出 DataFrame 的头部几行
print(df.head())

# 绘制 btc 价格曲线
df['ClosePrice'].plot(figsize=(14, 7))