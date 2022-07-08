#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
'''
@Author: lvmengting 
@Date: 2022-07-08 14:17:15
@Last Modified by:   lvmengting
@Last Modified time: 2022-07-08 14:17:15
'''

# Python内置的@property装饰器就是负责把一个方法变成属性调用的：


# class Student:

#     def get_score(self):
#         return self._score 

#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an int')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100')
#         self._score = value 


# s = Student()
# s.set_score(60)
# print(s.get_score())


'''
@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，
@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
'''

class Student:

    @property
    def score(self):
        return self._score 

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be a int')
        if value < 0 or value > 100:
            raise ValueError('score must be between 0 ~ 100')
        self._score = value 


