#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
'''
@Author: lvmengting 
@Date: 2022-07-08 16:38:40
@Last Modified by:   lvmengting
@Last Modified time: 2022-07-08 16:38:40
'''


'''
工厂方法适合对象种类较少的情况，如果有多种不同类型对象需要创建，使用抽象工厂模式。以实现一个游戏的例子说明，在一个抽象工厂类里实现多个关联对象的创建：
'''

class Frog:
    def __init__(self, name):
        self.name = name  

    def __str__(self) -> str:
        return self.name  

    def interact_with(self, obstcal):
        ''' 不同类型的玩家遇到的障碍不一样'''
        print(f'{self} the Frog encounters {obstcal} and {obstcal.action()}!')




class Bug:
    
    def __str__(self) -> str:
        return 'a bug'

    def action(self):
        return 'eats it'


class FrogWorld:
    
    def __init__(self, name):
        print(self)
        self.player_name = name 

    def __str__(self):
        return '\n\n\t----Forg World----'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard:
    
    def __init__(self, name) -> None:
        self.name = name 

    def __str__(self) -> str:
        return self.name  

    def interact_with(self, obstacle):
        print(f'{self} the Wizard battles a')





