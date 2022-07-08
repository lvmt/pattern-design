#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
'''
@Author: lvmengting 
@Date: 2022-07-08 10:14:39
@Last Modified by:   lvmengting
@Last Modified time: 2022-07-08 10:14:39
'''


'''
比较__new__ 和 __init__的差异
在研究具体的实现之前，我们应该知道 __new__ 方法只接受 cls 作为它的第一个参数，
而 __init__ 一个参数是 self (__new__ 是一个类方法，而__init__ 是一个对象方法)。
因为我们调用 __new__ 之前连实例都还没有，因此那时根本没有 self 的存在。
__init__ 在 使用 __new__ 创建并返回一个实例之后调用，因此可将返回的实例通过self传递给它。
'''

class A:

    def __new__(cls):
        print('A.__new__ called')
        return super(A, cls).__new__(cls)

    def __init__(self):
        print('A.__init__ called')


A()

