#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author:lvmengting
@Date:2022/07/21 15:40:07
'''

from abc import ABCMeta, abstractclassmethod




class WaterHeater:
    '''被监听对象'''
    
    def __init__(self):
        self.__observers = []
        self.__temperature = 25 
        
    def  get_temperature(self):
        return self.__temperature
    
    def set_temperature(self, temperature):
        self.__temperature = temperature
        print(f'当前温度是：{self.__temperature}')
        self.notifies()  # 被监听对象变化,就通知全部的观察者
        
    def add_observer(self, observer):
        self.__observers.append(observer)
        
    def notifies(self):
        for o in self.__observers:
            o.update(self)  # 更新最新消息
            
    
    
class Observer(metaclass=ABCMeta):
    
    '''洗澡模式和饮用水模式的父类'''
    @abstractclassmethod
    def update(self, waterheater):  # 传入监听对象
        pass 
    
    
    
class WashModel(Observer):
    
    def update(self, waterheater):
        if waterheater.get_temperature() >=50 and waterheater.get_temperature() < 70:
            print('水已经烧好了，温度正好，可以用来洗澡了')
            
            
            
class DrinkModel(Observer):
    
    def update(self, waterheater):
        if waterheater.get_temperature() >= 100:
            print('水已经烧开了，可以用来引用了')
            
            

def test_waterheater():
    heater = WaterHeater()
    washing_observer = WashModel()
    drinking_observer = DrinkModel()
    
    heater.add_observer(washing_observer)
    heater.add_observer(drinking_observer)
    heater.set_temperature(40)
    heater.set_temperature(60)
    heater.set_temperature(110)
    

test_waterheater()
    