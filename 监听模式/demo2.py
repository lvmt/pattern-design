#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author:lvmengting
@Date:2022/07/21 15:40:07
'''

from abc import ABCMeta, abstractclassmethod



class Oberser(metaclass=ABCMeta):
    
    '''观察者基类'''
    def update(self, observable, object):
        pass  
    
    

class Observerable:
    '被观察者基类'
    
    def __init__(self):
        self.__observers = []
        
    def add_observer(self, observer):
        self.__observers.append(observer)
        
    def remove_observer(self, observer):
        self.__observers.remove(observer)
        
    def notify_observers(self, object=0):
        for o in self.__observers:
            o.update(self, object)
            
            
            
class WaterHeater(Observerable):
    '''热水器'''
    
    def __init__(self):
        super().__init__()
        self.__temperature = 25 
        
    def  get_temperature(self):
        return self.__temperature
    
    def set_temperature(self, temperature):
        self.__temperature = temperature
        print(f'当前温度是：{self.__temperature}')
        self.notify_observers()  # 被监听对象变化,就通知全部的观察者
        
        
    
class WashingModel(Oberser):
    
    def update(self, observerable, object):
        if isinstance(observerable, WaterHeater) and \
            observerable.get_temperature() >= 50 and observerable.get_temperature() < 100:
            print('水已经烧好了, 温度正好，可以用来洗澡了')
            
    
    
class DrinkModel(Oberser):
    
    def update(self, observerable, object):
        if isinstance(observerable, WaterHeater) and \
            observerable.get_temperature() > 100:
            print('水已经烧开了，可以喝了')
            


if __name__ == '__main__':
    
    heater = WaterHeater()
    washing_observer = WashingModel()
    drinking_observer = DrinkModel()
    
    heater.add_observer(washing_observer)
    heater.add_observer(drinking_observer)
    
    heater.set_temperature(40)
    heater.set_temperature(60)
    heater.set_temperature(80)
    heater.set_temperature(110)
    
